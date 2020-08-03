import sys
sys.path.append('./')
from tools.generator_manager import *

year = '2017'

################################################################################
# Generate pure TH1 without fancy style 
################################################################################

'''
#MC
print 'Start Monte Carlo'

for i in range(len(sample_list['MC'][year])):
    generate_TH1('m_dilep', 50, 0, 800, year, 'MC', sample_list['MC'][year][i])
    print '----'

print ''




# DATA
print 'Start Data'

for i in range(len(sample_list['DATA'][year])):
    generate_TH1('m_dilep', 50, 0, 800, year, 'DATA', sample_list['DATA'][year][i])
    print '----'

print ''

'''


#SYST
print 'Start Systematics'

for i in range(len(sample_list['MC'][year])):
    for j in range(len(systematic_list)):
        generate_TH1_systematic('m_dilep', 50, 0, 800, year, systematic_list[j], 'Up', sample_list['MC'][year][i])
        generate_TH1_systematic('m_dilep', 50, 0, 800, year, systematic_list[j], 'Down',sample_list['MC'][year][i])
    print '----'

print ''