
##   PyPlotFramework

This framework is plotter based on pyROOT-CERN library. It was build for ttbar analysis.
PyPlotFramework is optimized for the CMS HEPPY output.

This framework is built with python2.7 !

# Installation :

In your terminal type following commands : 

    > git clone https://github.com/Arc-Pintade/PyPlotFramework.git

In the pyplotframework directory :

    > bash install.sh
    > source rootenv

NB: Caution, you need to have ROOT-CERN lirbary on your computer. And the rootenv 
need to be update (if needed) in function of your own ROOT installation path.


# Presentation of the framework 

This PyPlotFramework, is built in 2 part: 

  -> Build histograms from Heppy output rootfile, with reweight for MC samples and 
  triggers for Data. 

  These histograms are stored in :

    ./results/"year"/TH1

  -> Creation of combine input rootfile, comparaison data/mc plots, ...

  These results are stored in :

    ./results/"year"/combine
    ./results/"year"/stack
    ...

# Generate histograms, reweighted and triggered

    python ./bin/histograms_creator.py "year" "nature"

example : 

    python ./bin/histograms_creator.py 2016 DATA

NB: Caution it can be long ... (around 6 minutes)

# Comparaison Data/Monte-Carlo

Data/mc comparaison are created for a given observable

    python ./bin/comparaison_data_mc.py "observable" "year" "title"

example : 

    python ./bin/comparaison_data_mc.py m_dilep 2017 "Mass dileptonic"

# Combine input file creation 

Data/mc comparaison are created for a given observable

    python ./bin/combine.py "observable" "year" 

example :

    python ./bin/combine.py m_dilep 2017 

