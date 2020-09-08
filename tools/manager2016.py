
number_of_signal_samples_2016 = 2


def succeeds_job(percent):
    return 100./(percent)


events_N0_2016 = [
         4861272982.4,     # dilep       a
        32366940321.1,     # semilep     b
       1786575.621463,     # TTW         c 731877.673463 + 1054697.948
       1786575.621463,     # TTW         c
       3474799.985863,     # TTZ         d 502198.859443 + 1473733.63172 + 1498867.4947
       3474799.985863,     # TTZ         d
       3474799.985863,     # TTZ         d
        36768937.2554,     # STs         e
        31835781.3907,     # STt         f
        17771478.6534,     # STt~        g
         173908712.95,     # tW          h
        174109580.671,     # tw~         i
       7982310.323678,     # WW          j 994032.181008 + 6988278.14267
       7982310.323678,     # WW          j
            3997571.0,     # WZ          k 1000000.0 + 2997571.0
            3997571.0,     # WZ          k
            1996098.0,     # ZZ          l 990064.0 + 998034.0
            1996098.0,     # ZZ2         l
     40343467875130.0,     # WJets       m 3.68172226463e+12 + 3.66617456105e+13
     40343467875130.0      # WJets       m
]     


cross_sec_2016 = [ 
    89.048226,            # dilep       a
    366.91429,            # semilep     b
    0.2043,               # TTW         c
    0.2043,               # TTW         c
    0.2529,               # TTZ         d
    0.2529,               # TTZ         d
    0.2529,               # TTZ         d
    10.32,                # STs         e
    136.02,               # STt         f
    80.95,                # STt~        g
    35.85,                # tW          h
    35.85,                # tw~         i
    118.7,                # WW          j
    118.7,                # WW          j
    47.13,                # WZ          k
    47.13,                # WZ          k
    16.523,               # ZZ          l
    16.523,               # ZZ2         l
    61526.7,              # WJets       m
    61526.7,              # WJets       m
    #6225.4,               # DY          n
    #22635.14              # DY 10-50    o
    #22635.14              # DY 10-50    o
]

effective_mc_event_2016 = [ 
    succeeds_job(100.),    # dilep       a
    succeeds_job(100.),    # semilep     b
    succeeds_job(100.),    # TTW         c
    succeeds_job(100.),    # TTW         c
    succeeds_job(100.),    # TTZ         d
    succeeds_job(100.),    # TTZ         d
    succeeds_job(100.),    # TTZ         d
    succeeds_job(100.),    # STs         e
    succeeds_job(100.),    # STt         f
    succeeds_job(100.),    # STt~        g
    succeeds_job(100.),    # tW          h
    succeeds_job(100.),    # tw~         i
    succeeds_job(100.),    # WW          j
    succeeds_job(100.),    # WW          j
    succeeds_job(100.),    # WZ          k
    succeeds_job(100.),    # WZ          k
    succeeds_job(100.),    # ZZ          l
    succeeds_job(100.),    # ZZ2         l
    succeeds_job(100.),    # WJets       m
    succeeds_job(100.),    # WJets       m
    succeeds_job(100.),    # DY          n
    succeeds_job(100.),    # DY 10-50    o
    succeeds_job(100.),    # DY 10-50    o
]

effective_data_event_2016 = [ 
    succeeds_job(100.),    #MuonEG_B
    succeeds_job(100.),    #MuonEG_C
    succeeds_job(100.),    #MuonEG_D
    succeeds_job(100.),    #MuonEG_E
    succeeds_job(100.),    #MuonEG_F
    succeeds_job(100.),    #MuonEG_G
    succeeds_job(100.),    #MuonEG_H
    succeeds_job(100.),    #SingleElectron_B
    succeeds_job(100.),    #SingleElectron_C
    succeeds_job(100.),    #SingleElectron_D
    succeeds_job(100.),    #SingleElectron_E
    succeeds_job(100.),    #SingleElectron_F
    succeeds_job(100.),    #SingleElectron_G
    succeeds_job(100.),    #SingleElectron_H
    succeeds_job(100.),    #SingleMuon_B
    succeeds_job(100.),    #SingleMuon_C
    succeeds_job(100.),    #SingleMuon_D
    succeeds_job(100.),    #SingleMuon_E
    succeeds_job(100.),    #SingleMuon_F
    succeeds_job(100.),    #SingleMuon_G
    succeeds_job(100.)     #SingleMuon_H
]


################################################################################
# Trigger and systematics name list 
################################################################################


elecmu_trig_2016 = [
    'trg_muon_electron_mu23ele12_fired',
    'trg_muon_electron_mu23ele12DZ_fired',
    #'trg_muon_electron_mu12ele23_fired',
    #'trg_muon_electron_mu12ele23DZ_fired',
    'trg_muon_electron_mu8ele23_fired',
    'trg_muon_electron_mu8ele23DZ_fired'
]

mu_trig_2016 = [
    #'trg_muon_mu22eta21_fired',
    #'trg_muon_mutk22eta21_fired',
    'trg_muon_mu24_fired',
    'trg_muon_mutk24_fired'
]

elec_trig_2016 = [
    'trg_electron_ele27_fired',
    #'trg_electron_ele25eta21_fired',
    #'trg_electron_ele32eta21_fired'
]

SYST_PU = '0.046'

systematic_list = [
    'syst_elec_reco',
    'syst_elec_id',
    'syst_muon_id',
    'syst_muon_iso',
    'syst_em_trig',
    'syst_pu'
]
