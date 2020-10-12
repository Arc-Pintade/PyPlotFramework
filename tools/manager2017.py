

################################################################################
# Sample utilities
################################################################################

def succeeds_job(percent):
    return 100./(percent)

cross_sec_2017 = [
    118.7,    # WW
    47.13,    # WZ
    16.523,   # ZZ 
    89.05,    # dilep       
    364.31,   # semilep     
    380.11,   # hadronic    
    10.32,    # STs         
    10.32,    # STs2        
    136.02,   # STt  
    80.95,    # STt~ 
    35.5,     # tW          
    35.5,     # tW2         
    35.5,     # tW~         
    35.5,     # tw~2        
    0.2043,   # TTW         
    0.2043,   # TTW2        
    0.4062,   # TTW3        
    0.2529,   # TTZ         
    0.2529,   # TTZ2        
    0.5297,   # TTZ3        
    0.4062,   # WJets       
    0.4062,   # Wjets2      
    6225.4,   # DY        
    6225.4,   # DY2         
    22635.1   # DY 10-50     
]

'''
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
'''

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
