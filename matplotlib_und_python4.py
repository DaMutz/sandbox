#Import needed Modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
import matplotlib.font_manager
from pylab import *

filename = "test"

if __name__ == "__main__":
    
    print "Generating Graph"
    
    prop = matplotlib.font_manager.FontProperties(size=10) #Set Font Size
    
    data = csv2rec(filename + "-result.csv",delimiter=',') #Read csv File
    
    N = len(data['length_m']) #Get # of lengths
    Up_Exp = data['up_rate_expected_kbps'] #Read Data From Corresponding Columns
    Up_Meas = data['up_rate_measured_kbps']
    Down_Exp = data['ds_rate_expected_kbps']
    Down_Meas = data['ds_rate_measured_kbps']
    
    ind = np.arange(N)  # The X Locations
    
    fig = plt.figure() #Make Graph
    ax1 = fig.add_subplot(111)

    line1 = ax1.plot(ind, Up_Exp, color='b', ls='dashdot')
    line2 = ax1.plot(ind, Up_Meas, color='b')
    
    ax2 = ax1.twinx()
    line3 = ax2.plot(ind, Down_Exp, color='r', ls='dashdot')
    line4 = ax2.plot(ind, Down_Meas, color='r')
    
    for Up_Exp in ax1.get_yticklabels(): #Color for the US Values blue
        Up_Exp.set_color('b')
    
    for Down_Exp in ax2.get_yticklabels(): # Color for the DS Values red
        Down_Exp.set_color('r')
            
    ax1.set_ylim(ymin=0) #Start with 0 
    ax2.set_ylim(ymin=0) #Start with 0
    #ax1.yaxis.grid(color='grey', linestyle='dashed')
    #ax2.yaxis.grid(color='grey', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed') #For better orientation
    ax1.set_ylabel('Upstream Rate (kbps)')
    ax2.set_ylabel('Downstream Rate (kbps)')
    ax1.set_xticklabels(data['length_m'])
    ax1.set_title('Up- and Downstream Values')
        
    ax2.legend( (line1[0], line2[0], line3[0], line4[0]), ('Up (mandatory)', 'Up (measured)', 'Down (mandatory)', 'Down (measured)'), prop=prop, loc=0 )

    result_graph = filename + '-graph.png'
    savefig(result_graph)