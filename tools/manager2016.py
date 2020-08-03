
number_of_signal_samples_2016 = 2

def succeeds_job(percent):
    return 100./(percent)


cross_sec_2016 = [ 
    72.1,  #88.2,          # dilep       a
    300.9, #365.3,         # semilep     b
    0.1829,#0.2043,        # TTW         c
    0.1829,#0.2043,        # TTW         c
    0.2529,#               # TTZ         d
    0.2529,#               # TTZ         d
    0.2529,#               # TTZ         d
    3.74,  #3.36,          # STs         e
    136.02,#               # STt         f
    67.91, #80.95,         # STt~        g
    34.91, #35.9,          # tW          h
    34.91, #35.9,          # tw~         i
    63.21, #118.7,         # WW          j
    63.21, #118.7,         # WW          j
    22.82, #47.13,         # WZ          k
    22.82, #47.13,         # WZ          k
    10.32, #16.523,        # ZZ          l
    10.32, #16.523,        # ZZ2         l
    60290, #61526.7,       # WJets       m
    60290, #61526.7,       # WJets       m
    #5670,  #6025.2,       # DY          n
    #18590, #22635.14      # DY 10-50    o
    #18590  #22635.14      # DY 10-50    o
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
    succeeds_job(100.),    #SingleElectron_B
    succeeds_job(100.),    #SingleElectron_C
    succeeds_job(100.),    #SingleElectron_D
    succeeds_job(100.),    #SingleElectron_E
    succeeds_job(100.),    #SingleElectron_F
    succeeds_job(100.),    #SingleMuon_B
    succeeds_job(100.),    #SingleMuon_C
    succeeds_job(100.),    #SingleMuon_D
    succeeds_job(100.),    #SingleMuon_E
    succeeds_job(100.)     #SingleMuon_F
]


################################################################################
# Trigger and systematics name list 
################################################################################


elecmu_trig = [
    'trg_muon_electron_mu23ele12_fired',
    'trg_muon_electron_mu23ele12DZ_fired',
    #'trg_muon_electron_mu12ele23_fired',
    #'trg_muon_electron_mu12ele23DZ_fired',
    'trg_muon_electron_mu8ele23_fired',
    'trg_muon_electron_mu8ele23DZ_fired'
]

mu_trig = [
    #'trg_muon_mu22eta21_fired',
    #'trg_muon_mutk22eta21_fired',
    'trg_muon_mu24_fired',
    'trg_muon_mutk24_fired'
]

elec_trig = [
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
