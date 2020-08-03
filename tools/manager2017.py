

################################################################################
# Sample utilities
################################################################################

number_of_signal_samples_2017 = 2

def succeeds_job(percent):
    return 100./(percent)


cross_sec_2017 = [ 
    88.2,     # dilep       a
    365.3,    # semilep     b
    0.2043,   # TTW         c
    0.2529,   # TTZ         d
    3.36,     # STs         e
    136.02,   # STt         f
    80.95,    # STt~        g
    35.9,     # tW          h
    35.9,     # tw~         i
    118.7,    # WW          j
    47.13,    # WZ          k
    16.523,   # ZZ          l
    61526.7,  # WJets       m
    6025.2,   # DY          n
    22635.14  # DY 10-50    o
]

effective_mc_event_2017 = [
    succeeds_job(95.8),    # dilep       a
    succeeds_job(60.6),    # semilep     b
    succeeds_job(98.9),    # TTW         c
    succeeds_job(98.7),    # TTZ         d
    succeeds_job(95.9),    # STs         e
    succeeds_job(97.8),    # STt         f
    succeeds_job(100.),    # STt~        g
    succeeds_job(100.),    # tW          h
    succeeds_job(100.),    # tw~         i
    succeeds_job(100.),    # WW          j
    succeeds_job(100.),    # WZ          k
    succeeds_job(100.),    # ZZ          l
    succeeds_job(99.0),    # WJets       m
    succeeds_job(98.8),    # DY          n
    succeeds_job(100.)     # DY 10-50    o
]

effective_data_event_2017 = [
    succeeds_job(100.),    #MuonEG_B
    succeeds_job(100.),    #MuonEG_C
    succeeds_job(100.),    #MuonEG_D
    succeeds_job(95.8),    #MuonEG_E
    succeeds_job(100.),    #MuonEG_F
    succeeds_job(87.6),    #SingleElectron_B
    succeeds_job(100.),    #SingleElectron_C
    succeeds_job(100.),    #SingleElectron_D
    succeeds_job(83.3),    #SingleElectron_E
    succeeds_job(76.5),    #SingleElectron_F
    succeeds_job(100.),    #SingleMuon_B
    succeeds_job(100.),    #SingleMuon_C
    succeeds_job(100.),    #SingleMuon_D
    succeeds_job(100.),    #SingleMuon_E
    succeeds_job(100.)     #SingleMuon_F
]


################################################################################
# Trigger and systematics name list 
################################################################################

#AN 2019/228

elecmu_trig = [
    'trg_muon_electron_mu8ele23DZ_fired',
    'trg_muon_electron_mu12ele23DZ_fired',
    'trg_muon_electron_mu23ele12DZ_fired',
    'trg_muon_electron_mu23ele12_fired'
]

mu_trig = [
    'trg_muon_mu27_fired',
    'trg_muon_mu24eta21_fired'
]

elec_trig = [
    'trg_electron_ele35_fired',
#    'trg_electron_ele38_fired',
#    'trg_electron_ele40_fired',
#    'trg_electron_ele32doubleEG_fired'
]

systematic_list = [
    'syst_elec_reco',
    'syst_elec_id',
    'syst_muon_id',
    'syst_muon_iso',
    'syst_em_trig',
#    'syst_pu'
]