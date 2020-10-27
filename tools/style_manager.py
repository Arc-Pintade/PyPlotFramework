
pt_like_values  = [
    [50, 0, 250],               # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
eta_like_values = [
    [50, -3, 3],                # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
n_bjets_like_values = [
    [5, 0, 5],                  # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
n_jets_like_values = [
    [7, 0, 7],                  # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
rho_like_values = [
    [50, 0, 80],                # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
met_like_values = [
    [50, 0, 600],               # binning
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
m_dilep_like_values = [
    [50, 0, 800],               # binnings
    [0.65, 0.65, 0.87, 0.87]    # legend box
]
unix_time_like_values = [
    [1, 0, 1],               # binnings
    [0.65, 0.65, 0.87, 0.87]    # legend box
]

def observable_values(observable):
    if(observable.find('pt_') != -1): #changer ca
        return pt_like_values
    elif(observable.find('j1_pt') != -1): #changer ca
        return pt_like_values
    elif(observable.find('j2_pt') != -1): #changer ca
        return pt_like_values
    elif(observable.find('eta') != -1):
        return eta_like_values
    elif(observable.find('phi') != -1):
        return eta_like_values
    elif(observable.find('n_bjets') != -1):
        return n_bjets_like_values
    elif(observable.find('n_jets') != -1):
        return n_jets_like_values
    elif(observable.find('rho') != -1):
        return rho_like_values
    elif(observable.find('met') != -1):
        return met_like_values
    elif(observable.find('m_dilep') != -1):
        return m_dilep_like_values
    elif(observable.find('unix_time') != -1):
        return unix_time_like_values
    else:
        print 'no drawing parameters'


def style_ratioplot(ratio, title, limit):
    ratio.Draw("SAME")
    ratio.GetLowerRefYaxis().SetTitle(title)
    ratio.GetLowerRefYaxis().CenterTitle()
    ratio.GetLowerRefYaxis().SetLabelSize(0.03)
    ratio.GetLowerRefXaxis().SetLabelSize(0.03)

    ratio.GetLowerRefGraph().SetMaximum(1+limit)
    ratio.GetLowerRefGraph().SetMinimum(1-limit)



def style_labels_counting(histo, titleY, titleX):
    histo.GetXaxis().SetTitle(titleX)
    histo.GetXaxis().CenterTitle()
    histo.GetYaxis().SetTitle(titleY)
    histo.GetYaxis().CenterTitle()
    histo.GetYaxis().SetLabelSize(0.03)
    histo.GetYaxis().SetMaxDigits(4)
    histo.GetYaxis().SetTitleOffset(1.5)

def style_histo(histo, line_color, line_width, 
                       fill_color, fill_style, 
                      marker_size, marker_style=1):
    histo.SetLineColor(line_color)
    histo.SetLineWidth(line_width)
    histo.SetFillColor(fill_color)
    histo.SetFillStyle(fill_style)
    histo.SetMarkerSize(marker_size)
    histo.SetMarkerStyle(marker_style)

def legend_box(legend, coordinates):
    legend.SetX1(coordinates[0])
    legend.SetY1(coordinates[1])
    legend.SetX2(coordinates[2]) 
    legend.SetY2(coordinates[3])

###############################################################################
## CMS style 
###############################################################################
#import sys
#sys.path.append('./tools/CMS_style')
#
#from CMS_lumi import *
#from tdrstyle import *
#
#def CMS_style():
#    setTDRStyle()
#    CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
#    CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
#    CMS_lumi.writeExtraText = 1
#    CMS_lumi.extraText = "Supplementary"
#    CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only #plots (default is an empty string)
#    iPos = 11
#    if( iPos==0 ): CMS_lumi.relPosX = 0.12