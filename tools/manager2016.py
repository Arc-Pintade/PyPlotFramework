
number_of_signal_samples_2016 = 3


def succeeds_job(percent):
    return 100./(percent)


events_N0_2016 = [
         4861272982.4,     # dilep       a
        32366940321.1,     # semilep     b
        21500086465.2,     # hadronic    c
       1786575.621463,     # TTW         d 731877.673463 + 1054697.948 
       1786575.621463,     # TTW2        d
       569424.145342,      # TTW3        e 569424.145342
       3474799.985863,     # TTZ         f 502198.859443 + 1473733.63172 + 1498867.4947
       3474799.985863,     # TTZ2        f
       3474799.985863,     # TTZ3        f
        396340.932552,     # TTZ4        g
        #           1,     #TTG          h
        #           1,     #TTG2         h    
        36768937.2554,     # STs         i
        31835781.3907,     # STt         j
        17771478.6534,     # STt~        k
         173908712.95,     # tW          l
        174109580.671,     # tw~         m
       7982310.323678,     # WW          n 994032.181008 + 6988278.14267
       7982310.323678,     # WW          n
            3997571.0,     # WZ          o 1000000.0 + 2997571.0
            3997571.0,     # WZ          o
            1996098.0,     # ZZ          p 990064.0 + 998034.0
            1996098.0,     # ZZ2         p
     40343467875130.0,     # WJets       q 3.68172226463e+12 + 3.66617456105e+13
     40343467875130.0      # WJets       q
    #1,                    # DY          r
    #1,                    # DY 10-50    s
    #1,                    # DY 10-50    s
    #1                     # DY 10-50    s
]     


cross_sec_2016 = [ 
    89.048226,            # dilep       a
    366.91429,            # semilep     b
    377.96006,            # hadronic    c
    0.2043,               # TTW         d
    0.2043,               # TTW2        d
    0.4062,               # TTW3        e
    0.2529,               # TTZ         f
    0.2529,               # TTZ2        f
    0.2529,               # TTZ3        f
    0.5297,               # TTZ4        g
    #3.697,                # TTG         h
    #3.697,                # TTG2        h 
    10.32,                # STs         i
    136.02,               # STt         j
    80.95,                # STt~        k
    35.85,                # tW          l
    35.85,                # tw~         m
    118.7,                # WW          n
    118.7,                # WW2         n
    47.13,                # WZ          o
    47.13,                # WZ2         o
    16.523,               # ZZ          p
    16.523,               # ZZ2         p
    61526.7,              # WJets       q
    61526.7,              # WJets2      q
    #6225.4,               # DY          r
    #22635.14              # DY 10-50    s
    #22635.14              # DY 10-50    s
    #22635.14              # DY 10-50    s
]

effective_mc_event_2016 = [ 
    succeeds_job(100.),    # dilep       a
    succeeds_job(100.),    # semilep     b
    succeeds_job(100.),    # hadronic    c 
    succeeds_job(100.),    # TTW         d
    succeeds_job(100.),    # TTW2        d
    succeeds_job(100.),    # TTW3        e
    succeeds_job(100.),    # TTZ         f
    succeeds_job(100.),    # TTZ2        f
    succeeds_job(100.),    # TTZ3        f
    succeeds_job(100.),    # TTZ4        g
    #succeeds_job(0.),      # TTG         h
    #succeeds_job(0.),      # TTG2        h
    succeeds_job(100.),    # STs         i
    succeeds_job(100.),    # STt         j
    succeeds_job(100.),    # STt~        k
    succeeds_job(100.),    # tW          l
    succeeds_job(100.),    # tw~         m
    succeeds_job(100.),    # WW          n
    succeeds_job(100.),    # WW          n
    succeeds_job(100.),    # WZ          o
    succeeds_job(100.),    # WZ          o
    succeeds_job(100.),    # ZZ          p
    succeeds_job(100.),    # ZZ2         p
    succeeds_job(100.),    # WJets       q
    succeeds_job(100.),    # WJets       q
    #succeeds_job(100.),    # DY          r
    #succeeds_job(100.),    # DY 10-50    s
    #succeeds_job(100.),    # DY 10-50    s
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

trig_2016 = [
    'trg_muon_electron_mu23ele12_fired',
    'trg_muon_electron_mu23ele12DZ_fired',
    'trg_muon_electron_mu8ele23_fired',
    'trg_muon_electron_mu8ele23DZ_fired',
    'trg_muon_mu24_fired',
    'trg_muon_mutk24_fired',
    'trg_electron_ele27_fired'
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