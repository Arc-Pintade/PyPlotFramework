from directory_manager import *

from manager2016 import *
from manager2017 import *

sample_list_MC_2016 = inputs_name('inputs', '2016', 'MC')
sample_list_MC_2017 = inputs_name('inputs', '2017', 'MC')
#sample_list_MC_2018 = inputs_name('inputs', '2018', 'MC')
sample_list_DATA_2016 = inputs_name('inputs', '2016', 'DATA')
sample_list_DATA_2017 = inputs_name('inputs', '2017', 'DATA')
#sample_list_DATA_2018 = inputs_name('inputs', '2018', 'DATA')

sample_list_MC = {
    '2016' : sample_list_MC_2016,
    '2017' : sample_list_MC_2017,
#    '2018' : sample_list_MC_2018
}

sample_list_DATA = {
    '2016' : sample_list_DATA_2016,
    '2017' : sample_list_DATA_2017,
#    '2018' : sample_list_DATA_2018
}

elecmu_trig =  {
    '2016' : elecmu_trig_2016,
    '2017' : elecmu_trig_2017,
#    '2018' : elecmu_trig_2018
}

mu_trig = {
    '2016' : mu_trig_2016,
    '2017' : mu_trig_2017,
#    '2018' : mu_trig_2018
}

elec_trig = {
    '2016' : elec_trig_2016,
    '2017' : elec_trig_2017,
#    '2018' : elec_trig_2018
}


# To call sample_list do sample_list[nature][year]
sample_list = {
    'MC'   : sample_list_MC,
    'DATA' : sample_list_DATA
}



################################################################################
# Utils
################################################################################

def index(year, sample, dataset='MC'):
    foo = 0
    for i in sample_list[dataset][year]:
        if(i == sample):
            return foo
        foo += 1 

def sum_of_weight(year, sample):
    filterfile = eventfilter_input(year, 'MC', sample,
        'CMGTools.TTbarTime.heppy.analyzers.MCWeighter.MCWeighter_MCWeighter')
    event = []
    f = open(filterfile, 'r')
    for i in f.read().split():
        try:
            event.append(float(i.strip()))
        except:
            pass
    return event[3]

def percent(x, total):
    return round(100.* x/total, 2)

################################################################################
# Variables
################################################################################

#events_N0_2016 = []
#for i in range(len(cross_sec_2016)):
#    events_N0_2016.append(sum_of_weight('2016',sample_list['MC']['2016']#[i])
#                          *effective_mc_event_2016[i])
#
#events_N0_2017 = []
#for i in range(len(cross_sec_2017)):
#    events_N0_2017.append(sum_of_weight('2017',sample_list['MC']['2017']#[i])
#                          *effective_mc_event_2017[i])

effective_data_event = {
    '2016' : effective_data_event_2016,
    '2017' : effective_data_event_2017,
    '2018' : 35.9,
}

number_of_signal_samples = {
    '2016' : number_of_signal_samples_2016,
    '2017' : number_of_signal_samples_2017,
    '2018' : 35.9,
}

luminosity = {
    '2016' : 35.9,
    '2017' : 41.53,
    '2018' : 0
}

cross_sec = {
    '2016' : cross_sec_2016,
    '2017' : cross_sec_2017,
    '2018' : 0
}

events_N0 = {
    '2016' : events_N0_2016,
    '2017' : events_N0_2017,
    '2018' : 0
}


def mc_rescale(year, sample):
    foo = 1000.*luminosity[year]*cross_sec[year][index(year, sample)]
    return foo/(events_N0[year][index(year, sample)])
