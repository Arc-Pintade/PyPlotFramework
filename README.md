
##   PyPlotFramework

This framework is plotter based on pyROOT-CERN library. It was build for ttbar analysis.
PyPlotFramework is optimized for the CMS HEPPY output.

# Installation :

In your terminal type following commands : 

    > git clone https://github.com/Arc-Pintade/PyPlotFramework.git
    > bash install.sh

# Comparaison Data/Monte-Carlo : 

    python ./bin/comparaison_data_mc.py "observable" "year" "title"

example : 

    python ./bin/comparaison_data_mc.py m_dilep 2017 "Mass dileptonic"

# Combine input file creation 

    python ./bin/combine.py "observable" "year" 

example :

    python ./bin/combine.py m_dilep 2017 

