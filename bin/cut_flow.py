import sys
sys.path.append('./')
from tools.generator_manager import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year', help='year of samples')

args = parser.parse_args()
year = args.year



################################################################################

def event_filtered(file, is_after = True):
    event = []
    f = open(file, 'r')
    for i in f.read().split():
        try:
            event.append(int(i.strip()))
        except:
            pass
    if(is_after):
        return event[1]
    else:
        return event[0]

def cut_flow_human_readable(filter, year):
    filter_h = []
    if(year == '2016'):
        filter_h.append() #signal
        #filter_h.append(filter[13]+filter[14]) #Zjets
    elif(year == '2017'):
        filter_h.append(filter[0]+filter[1]) #signal
        filter_h.append(filter[2]+filter[3]+filter[4]+filter[5]
                       +filter[6]+filter[7]+filter[8]+filter[9]) #TTX
        filter_h.append(filter[10]+filter[11]+filter[12]+filter[13]+filter[14]) #ST
        filter_h.append(filter[15]+filter[16]) #diboson
        filter_h.append(filter[17]+filter[18]) #Wjets
        filter_h.append(filter[19]) #Zjets
    return filter_h


################################################################################

onebjet = 'OneBJets'
onedilep = 'OneDilepton'
twojets = 'TwoJets'


full         = []
one_bjet     = []
one_dilepton = []
two_jets     = []


for i in sample_list['MC'][year]:
    full.append(event_filtered(efficiency_input(year,'MC', i, onedilep), False))
    one_dilepton.append(event_filtered(efficiency_input(year,'MC', i, onedilep), True))
    two_jets.append(event_filtered(efficiency_input(year,'MC', i, twojets), True))
    one_bjet.append(event_filtered(efficiency_input(year,'MC', i, onebjet), True))


integrals = []

rootfile = []
for i in range(len(sample_list['MC'][year])):
    namefile = sample_list['MC'][year][i]+'_'+'m_dilep'+'.root'
    rootfile.append(TFile(results_path(year,'TH1/MC',namefile)))
    foo = rootfile[i].Get('m_dilep')
    integrals.append(foo.Integral())
del rootfile


name_channel_h = [
    '$t\\bar{t}$ signal',
    'TTX',
    'single top',
    'dibosons',
    'W$+$Jets',
    'Z$+$Jets'
]

integrals_h    = cut_flow_human_readable(integrals, year)
full_h         = cut_flow_human_readable(full, year)
one_bjet_h     = cut_flow_human_readable(one_bjet, year)
one_dilepton_h = cut_flow_human_readable(one_dilepton, year)
two_jets_h     = cut_flow_human_readable(two_jets, year)

to_one_dilep = []
to_two_jets = []
to_one_bjets = []

for i in range(len(full_h)):
    to_one_bjets.append(two_jets_h[i]/float(one_bjet_h[i]))
    to_two_jets.append(one_dilepton_h[i]/float(one_bjet_h[i]))
    to_one_dilep.append(full_h[i]/float(one_bjet_h[i]))

for i in range(len(integrals_h)):
    print name_channel_h[i]+' full > '+str(to_one_dilep[i]*integrals_h[i])
    print name_channel_h[i]+' one dilep > '+str(to_two_jets[i]*integrals_h[i])
    print name_channel_h[i]+' two jets > '+str(to_one_bjets[i]*integrals_h[i])
    print name_channel_h[i]+' one bjets > '+str(integrals_h[i])
    print '---'