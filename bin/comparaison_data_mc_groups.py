#!/usr/bin/env python

import sys
sys.path.append('./')

from tools.directory_manager import *
from tools.sample_manager import *
from tools.style_manager import *

import argparse

from ROOT import TFile, TH1, TCanvas, TH1F, THStack 
from ROOT import TLegend, TApplication, TRatioPlot, TPad

################################################################################
## Initialisation stuff
################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('observable', help='display your observable')
parser.add_argument('year', help='year of samples')
parser.add_argument('title', help='display your observable title')
parser.add_argument('subtitle',nargs='?', help='display your observable subtitle', default='')

args = parser.parse_args()
observable = args.observable
year = args.year
title = args.title
subtitle = args.subtitle
if(subtitle == ''):
    if year=='2016':
        subtitle = '35.9 fb^{-1} (13TeV)'
    elif year=='2017':
        subtitle = '41.53 fb^{-1} (13TeV)'

nbin = 0
min_bin = 0
max_bin = 0
legend_coordinates = observable_values(observable)[1]
TH1.SetDefaultSumw2(1)
mc_integral = 0
data_integral = 0
canvas = TCanvas('stack_'+observable,'stack_'+observable, 1000, 800)

################################################################################
## Create Histo 
################################################################################


# mc_signal
rootfile_signal = TFile(results_path(year,'groups/MC',"signal_"+observable+".root"))
hist_signal = rootfile_signal.Get('signal_'+observable)
mc_integral += hist_signal.Integral()

# convenient variables
nbin    = hist_signal.GetNbinsX()
min_bin = hist_signal.GetXaxis().GetXmin()
max_bin = hist_signal.GetXaxis().GetXmax()



# mc_background
hist_background = TH1F("","", nbin, min_bin, max_bin)
rootfile = []
i = 0
for sample in sample_list_groups[year]:
    hist_name = sample[:-5] # '.root' 5 char
    if(sample.find('signal') == -1 and sample.find(observable) != -1):
        print sample, hist_name
        rootfile.append(TFile(results_path(year,'groups/MC',sample)))
        foo = rootfile[i].Get(hist_name)
        print foo.Integral()
        mc_integral += foo.Integral()
        hist_background.Add(foo)
        i = i+1
del rootfile


# data
hist_data = TH1F("","", nbin, min_bin, max_bin)
rootfile = []
for i in range(len(sample_list['DATA'][year])):
    namefile = sample_list['DATA'][year][i]+'_'+observable+'.root'
    rootfile.append(TFile(results_path(year,'TH1/DATA',namefile)))
    foo = rootfile[i].Get(observable)
    data_integral += foo.Integral()
    hist_data.Add(foo)
del rootfile


################################################################################
## Draw stuff
################################################################################
'''
hist_mc = TH1F("","", nbin, min_bin, max_bin)
hist_mc.Add(hist_background)
hist_mc.Add(hist_signal)
#hist_mc.Draw("E HIST")
hist_background.Draw("E SAME")
hist_data.Draw("E SAME")
'''
stack = THStack()
stack.Add(hist_background)
stack.Add(hist_signal)
stack.Draw("E HIST")
hist_data.Draw("E SAME")

################################################################################
## Set Style
################################################################################

# line_color, line_width, fill_style, marker_style
style_histo(hist_signal, 2, 1, 2, 3004, 0)
style_histo(hist_background, 4, 1, 4, 3005, 0)
style_histo(hist_data, 1, 1, 0, 3001, 1, 20)

################################################################################
## Save
################################################################################

newfile = TFile(results_path(year,'stack',observable+'_groups.root'), 'RECREATE')
canvas.Update()
canvas.Write()
newfile.Close()
canvas.SaveAs(results_path(year,'stack',observable+'_groups.png'))

print ''
print "Data : ", data_integral
print "MC : ", mc_integral
print "Ratio MC/DATA : ", percent(mc_integral,data_integral),'%'
print ''

exit = raw_input("Press key to quit : ") 

