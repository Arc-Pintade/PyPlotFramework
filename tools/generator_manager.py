from directory_manager import *
from sample_manager import *
from tools.style_manager import *

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

def generate_systematics(tree, up_down):
    foo = 1.
    for syst in systematic_list:
        if up_down == 'up':
            foo *= (1+tree.GetLeaf(syst).GetValue())
        elif up_down == 'down':
            foo *= (1-tree.GetLeaf(syst).GetValue())
        else:
            print 'error in systematics extration'
            exit()
    # pu systematic
    foo *= tree.GetLeaf('weight_pu_'+up_down).GetValue()
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

def read_DATA_variable(year, tree, variable, file_name):
    number = 0
    if(trigger_passed(tree, triggers[year])):
        if (file_name.find('MuonEG')!=-1):
            number = tree.GetLeaf(variable).GetValue()
            return number
            if (file_name.find('SingleMuon')!=-1):
                number = tree.GetLeaf(variable).GetValue()
                return number
                if (file_name.find('SingleElectron')!=-1):
                    number = tree.GetLeaf(variable).GetValue()
                    return number
    return number


# for syst
def generate_syst(tree, systematic_name, up_down):
    foo = tree.GetLeaf(systematic_name).GetValue()
    if(up_down == 'Up'):
        return 1+foo
    elif(up_down == 'Down'):
        return 1-foo
    else:
        print 'up_down error'

def write(hist, variable, year, where, nature, sample):
    newfile = TFile(file_inout('results', year, where, nature , sample+'_'+variable+'.root'), 'RECREATE')
    hist.Write()
    newfile.Close()


################################################################################
# For groups
################################################################################

def grouping(n_bin, bin_min, bin_max, year, hist, grp):
    foo = [[] for x in xrange(len(analysis_list[year]))]
    for h in hist:
        for i in range(len(h)):
            h[i].append(TH1F(grp+var, var, n_bin, bin_min, bin_max))
            for index, grp in enumerate(analysis_list):
                if(h[i].GetName().find(grp)!=-1):
                    foo[i][index] += h[i][index]
        return False


################################################################################
################################################################################
################################################################################

def generate_MC_groups(year, variables_list, analysis_list):

   #hist = [[] for x in xrange(len(sample_list_DATA[year]))]
    hist = []
    hist_syst_up = []
    hist_syst_down = []
    for ind, grp in enumerate(analysis_list):
        hist.append([])
        hist_syst_up.append([])
        hist_syst_down.append([])
        for var in variables_list:
            binning = observable_values(var)[0]
            hist[ind].append(TH1F(grp+'_'+var, var, binning[0], binning[1], binning[2]))
            hist_syst_up[ind].append(TH1F(grp+'_'+var+'Up', var, binning[0], binning[1], binning[2]))
            hist_syst_down[ind].append(TH1F(grp+'_'+var+'Down', var, binning[0], binning[1], binning[2]))

    for sample_index, sample in enumerate(sample_list['MC'][year]):
        rfile  = TFile(heppy_tree(year, 'MC', sample))
        tree   = rfile.Get('events')
        h      = []
        h_up   = []
        h_down = []
        for var in variables_list:
            binning = observable_values(var)[0]
            h.append(TH1F(sample+'_'+var, var, binning[0], binning[1], binning[2]))
            h_up.append(TH1F(sample+'_'+var+'Up', var, binning[0], binning[1], binning[2]))
            h_down.append(TH1F(sample+'_'+var+'Down', var, binning[0], binning[1], binning[2]))
        for i in range(tree.GetEntriesFast()):
            tree.GetEntry(i)
            sf_weight   = generate_weight(tree)
            syst_up = generate_systematics(tree, 'up')
            syst_down = generate_systematics(tree, 'down')
            if(trigger_passed(tree, triggers[year])):
                for ind, var in enumerate(variables_list):
                    h[ind].Fill(tree.GetLeaf(var).GetValue(),sf_weight)
                    h_up[ind].Fill(tree.GetLeaf(var).GetValue(),sf_weight*syst_up)
                    h_down[ind].Fill(tree.GetLeaf(var).GetValue(),sf_weight*syst_down)
            if(i%100000 == 0):
                print '100 000 events passed'
        for i in range(len(variables_list)):
            h[i].Scale(mc_rescale(year, sample))
            h_up[i].Scale(mc_rescale(year, sample))
            h_down[i].Scale(mc_rescale(year, sample))

            for grp_index, grp in enumerate(analysis_list):
                if(h[i].GetName().find(grp) != -1):
                    hist[grp_index][i].Add(h[i])
                    hist_syst_up[grp_index][i].Add(h_up[i])
                    hist_syst_down[grp_index][i].Add(h_down[i])
        print 'next sample'

    for grp_i, grp in enumerate(analysis_list):
        for var_i, var in enumerate(variables_list):
            write(hist[grp_i][var_i], var, year, 'groups', 'MC', grp)
            write(hist_syst_up[grp_i][var_i], var+'Up', year, 'groups', 'SYST', grp)
            write(hist_syst_down[grp_i][var_i], var+'Down', year, 'groups', 'SYST', grp)


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
        hist.Scale(effective_data_event[year][index(year,sample,'DATA')])
    ########################
    write(hist, variable, year, 'TH1', nature, sample)
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