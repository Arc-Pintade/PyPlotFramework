#!/usr/bin/env python

import sys
sys.path.append('./')

from tools.directory_manager import *
from tools.sample_manager import *
from tools.style_manager import *
from tools.generator_manager import *

import argparse

from ROOT import TFile, TH1, TCanvas, TH1F, THStack 
from ROOT import TLegend, TApplication, TRatioPlot, TPad


################################################################################
## Initialisation stuff
################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('year', help='year of samples')

args = parser.parse_args()
year = args.year


timestamp = []

for sample in sample_list['DATA'][year]:
    rfile = TFile(heppy_tree(year, 'DATA', sample))
    tree  = rfile.Get('events')
    for i in range(tree.GetEntriesFast()):
        tree.GetEntry(i)
        timestamp.append(read_DATA_variable(year, tree, 'unix_time', sample))

with open('./results/timestamp'+year+'.txt', 'w') as f:
    for item in timestamp:
        print >> f, item