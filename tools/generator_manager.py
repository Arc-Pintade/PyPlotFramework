from directory_manager import *
from sample_manager import *

from multiprocessing import Pool

from ROOT import TFile, TH1F

################################################################################
# General
################################################################################

# for MC
def generate_weight(tree):
    foo = 1.
    foo *= tree.GetLeaf('weight_pu').GetValue()
    foo *= tree.GetLeaf('weight_generator').GetValue()
    foo *= tree.GetLeaf('weight_top').GetValue()
    #lepton
    foo *= tree.GetLeaf('weight_sfe_id').GetValue()
    foo *= tree.GetLeaf('weight_sfe_reco').GetValue()
    foo *= tree.GetLeaf('weight_sfm_id').GetValue()
    foo *= tree.GetLeaf('weight_sfm_iso').GetValue()
    #hadron
    for i in range(int(tree.GetLeaf('n_bjets').GetValue())):
        foo *= tree.GetLeaf('weight_sfb').GetValue()
    #trigger
    foo *= tree.GetLeaf('weight_sf_em_trig').GetValue()
    return foo

# for DATA
def trigger_passed(tree, trigger_list):
    trig = 0
    for l in trigger_list:
        if(tree.GetLeaf(l).GetValue() == 1):
            trig += 1
    if(trig>1):
        return True
    return False


def generate_trigger(year, tree, hist, variable, file_name):
    if(trigger_passed(tree, triggers[year])):
        if (file_name.find('MuonEG')!=-1):
            hist.Fill(tree.GetLeaf(variable).GetValue())
            return
            if (file_name.find('SingleMuon')!=-1):
                hist.Fill(tree.GetLeaf(variable).GetValue())
                return
                if (file_name.find('SingleElectron')!=-1):
                    hist.Fill(tree.GetLeaf(variable).GetValue())
                    return
    return
'''
def generate_trigger(year, tree, hist, variable, file_name):
    if(trigger_passed(tree, elecmu_trig[year])):
        if (file_name.find('MuonEG')!=-1):
            hist.Fill(tree.GetLeaf(variable).GetValue())
        return
    if(trigger_passed(tree, mu_trig[year]) and file_name.find('SingleMuon')!=-1):
        print file_name, tree.GetLeaf(variable).GetValue()
        hist.Fill(tree.GetLeaf(variable).GetValue())
        return
    if(trigger_passed(tree, elec_trig[year]) and file_name.find('SingleElectron')!=-1):
        hist.Fill(tree.GetLeaf(variable).GetValue())
        return
    return
'''

# for syst
def generate_syst(tree, systematic_name, up_down):
    foo = tree.GetLeaf(systematic_name).GetValue()
    if(up_down == 'Up'):
        return 1+foo
    elif(up_down == 'Down'):
        return 1-foo
    else:
        print 'up_down error'

def write(hist, variable, year, nature, sample):
    newfile = TFile(file_inout('results', year, 'TH1', nature , sample+'_'+variable+'.root'), 'RECREATE')
    hist.Write()
    newfile.Close()

################################################################################
################################################################################
################################################################################

def generate_TH1(variable, n_bin, bin_min, bin_max, 
                    year, nature, sample):
    rfile = TFile(heppy_tree(year, nature, sample))
    hist  = TH1F(variable, variable, n_bin, bin_min, bin_max)
    tree  = rfile.Get('events')

    ########################
    if(nature == 'MC'):
        
        for i in range(tree.GetEntriesFast()):
            tree.GetEntry(i)
            sf_weight   = generate_weight(tree)
            if(trigger_passed(tree, triggers[year])):
                hist.Fill(tree.GetLeaf(variable).GetValue(),sf_weight)
            if(i%100000 == 0):
                print '100 000 events passed'
        hist.Scale(effective_mc_event[year][index(year,sample,'MC')])
        hist.Scale(mc_rescale(year, sample))
    ########################
    elif(nature == 'DATA'):
        for i in range(tree.GetEntriesFast()):
            tree.GetEntry(i)
            generate_trigger(year, tree, hist, variable, sample)
            '''
            if(trigger_passed(tree, elecmu_trig[year])):
                if (sample.find('MuonEG')!=-1):
                    hist.Fill(tree.GetLeaf(variable).GetValue())
                continue
            if(trigger_passed(tree, mu_trig[year]) and sample.find('SingleMuon')!=-1):
                hist.Fill(tree.GetLeaf(variable).GetValue())
                continue
            if(trigger_passed(tree, elec_trig[year]) and sample.find('SingleElectron')!=-1):
                hist.Fill(tree.GetLeaf(variable).GetValue())
                continue
            '''
        hist.Scale(effective_data_event[year][index(year,sample,'DATA')])
    ########################
    write(hist, variable, year, nature, sample)
    rfile.Close()


def generate_TH1_systematic(variable, n_bin, bin_min, bin_max, year, systematic_name, up_down, sample):
    rfile = TFile(heppy_tree(year, 'MC', sample))
    hist  = TH1F(variable, variable, n_bin, bin_min, bin_max)
    tree  = rfile.Get('events')

    for i in range(tree.GetEntriesFast()):
        tree.GetEntry(i)
        sf_weight   = generate_weight(tree)
        syst_weight = generate_syst(tree, systematic_name, up_down)
        hist.Fill(tree.GetLeaf(variable).GetValue(),sf_weight*syst_weight)
        if(i%100000 == 0):
            print '100 000 events passed'
    hist.Scale(mc_rescale(year, sample))

    newfile = TFile(file_inout('results', year, 'TH1', 'SYST' , sample+'_'+variable+'_'+systematic_name+up_down+'.root'), 'RECREATE')
    hist.Write()
    newfile.Close()
    rfile.Close()