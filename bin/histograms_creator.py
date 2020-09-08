import sys
sys.path.append('./')
from tools.generator_manager import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year', help='year of samples')
parser.add_argument('nature', help='DATA, MC, SYST')

args = parser.parse_args()
year = args.year
nature = args.nature

################################################################################
# Generate pure TH1 without fancy style 
################################################################################


#MC
if nature == "MC":
    print 'Start Monte Carlo'

    for i in range(len(sample_list['MC'][year])):
        generate_TH1('m_dilep', 50, 0, 800, year, 'MC', sample_list['MC'][year][i])
        print '----'

    print ''


# DATA
elif nature == "DATA":
    print 'Start Data'

    for i in range(len(sample_list['DATA'][year])):
        generate_TH1('m_dilep', 50, 0, 800, year, 'DATA', sample_list['DATA'][year][i])
        print '----'

    print ''


#SYST
elif nature == "SYST":
    print 'Start Systematics'

    for i in range(len(sample_list['MC'][year])):
        for j in range(len(systematic_list)):
            generate_TH1_systematic('m_dilep', 50, 0, 800, year, systematic_list[j], 'Up', sample_list['MC'][year][i])
            generate_TH1_systematic('m_dilep', 50, 0, 800, year, systematic_list[j], 'Down',sample_list['MC'][year][i])
        print '----'

    print ''

else:
    print "Wrong nature of sample (DATA, MC, SYST)"