

################################################################################
# Sample utilities
################################################################################

number_of_signal_samples_2017 = 3


def succeeds_job(percent):
    return 100./(percent)



events_N0_2017 = [
4984888995.13,     # dilep       a
21291094704.9,     # semilep     b
40875369044.7,      # hadronic    c
3961558.21994,     # TTW         d  1711122.8415+1690120.24502+560315.13342
3961558.21994,     # TTW2        e
3961558.21994,     # TTW3        f
5006014.1531340005,     # TTZ         g 1928279.37186 + 2694672.71263 + 383062.068644
5006014.1531340005,     # TTZ2        h
5006014.1531340005,     # TTZ3        i
114743635.4945,     # TTG         j  52378708.8009 + 62364926.6936
114743635.4945,     # TTG2        k
      # STs         l
35616718.0712,     # STs2        m
5919651.0,     # STt         n
3675910.0,     # STt~        o
      # tW          p
277241050.839,     # tW2         q
      # tW~         r
270762750.172,     # tw~2        s
      # WW          t
3928630.0,     # WZ          u
1925931.0,     # ZZ          v
58536004.0,     # WJets       w  33043732.0 + 25492272.0
58536004.0,     # Wjets2      x
3498589972354.0,      # DY          y  4.89144918014e+11 + 3.00944505434e+12
3498589972354.0,     # DY2         z
11599648.0     # DY 10-50     zz
]

cross_sec_2017 = [ 
    89.05,    # dilep       a
    364.31,   # semilep     b
    380.11,   # hadronic    c
    0.2043,   # TTW         d
    0.2043,   # TTW2        e
    0.4062,   # TTW3        f
    0.2529,   # TTZ         g
    0.2529,   # TTZ2        h
    0.5297,   # TTZ3        i
    3.697,    # TTG         j
    3.697,    # TTG2        k
#    10.32,    # STs         l
    10.32,    # STs2        m
    136.02,   # STt         n
    80.95,    # STt~        o
#    35.5,     # tW          p
    35.5,     # tW2         q
#    35.5,     # tW~         r
    35.5,     # tw~2        s
#    118.7,    # WW          t
    47.13,    # WZ          u
    16.523,   # ZZ          v
    0.4062,   # WJets       w
    0.4062,   # Wjets2      x
    6225.4,   # DY          y
    6225.4,   # DY2         z
    22635.1  # DY 10-50     zz
]

effective_mc_event_2017 = [
    succeeds_job(100.),   # dilep       a
    succeeds_job(64.4),   # semilep     b
    succeeds_job(100.),   # hadronic    c
    succeeds_job(100.),   # TTW         d
    succeeds_job(100.),   # TTW2        e
    succeeds_job(100.),   # TTW3        f
    succeeds_job(100.),   # TTZ         g
    succeeds_job(100.),   # TTZ2        h
    succeeds_job(100.),   # TTZ3        i
    succeeds_job(100.),   # TTG         j
    succeeds_job(100.),   # TTG2        k
#    succeeds_job(100.),   # STs         l
    succeeds_job(95.9),   # STs2        m
    succeeds_job(98.9),   # STt         n
    succeeds_job(100.),   # STt~        o
#    succeeds_job(100.),   # tW          p
    succeeds_job(100.),   # tW2         q
#    succeeds_job(100.),   # tW~         r
    succeeds_job(100.),   # tw~2        s
#    succeeds_job(100.),   # WW          t
    succeeds_job(100.),   # WZ          u
    succeeds_job(100.),   # ZZ          v
    succeeds_job(100.),   # WJets       w
    succeeds_job(59.1),   # Wjets2      x
    succeeds_job(100.),   # DY          y
    succeeds_job(91.7),   # DY2         z
    succeeds_job(31.2   ),  # DY 10-50     zz
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

elecmu_trig_2017 = [
    'trg_muon_electron_mu8ele23DZ_fired',
#    'trg_muon_electron_mu12ele23DZ_fired',
#    'trg_muon_electron_mu23ele12DZ_fired',
    'trg_muon_electron_mu23ele12_fired'
]

mu_trig_2017 = [
    'trg_muon_mu27_fired',
#    'trg_muon_mu24eta21_fired'
]

elec_trig_2017 = [
    'trg_electron_ele35_fired',
#    'trg_electron_ele38_fired',
#    'trg_electron_ele40_fired',
#    'trg_electron_ele32doubleEG_fired'
]

trig_2017 = [
    'trg_muon_electron_mu8ele23DZ_fired',
    'trg_muon_electron_mu23ele12_fired',
    'trg_muon_mu27_fired',
    'trg_electron_ele35_fired'
]


systematic_list = [
    'syst_elec_reco',
    'syst_elec_id',
    'syst_muon_id',
    'syst_muon_iso',
    'syst_em_trig',
#    'syst_pu'
]