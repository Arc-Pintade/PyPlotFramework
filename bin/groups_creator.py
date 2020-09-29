import sys
sys.path.append('./')
from tools.generator_manager import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year', help='year of samples')

args = parser.parse_args()
year = args.year

################################################################################
# Variables
################################################################################

variables = [
    'm_dilep',
    'n_bjets'
]

################################################################################
# Generate pure TH1 without fancy style 
################################################################################

generate_MC_groups(20,0,250, year, variables, ttbar_list)
