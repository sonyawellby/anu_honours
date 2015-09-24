#from plot import multi
from cwd import cwdInFunction
cwdInFunction()

from matplotlib import pyplot as plt
import glob
import matplotlib.image as mpimg
import pylab

num = "1_sd"

def multi(directory,nrow,ncol,title=''):
    """
    A file to plot nine pre-plotted images in a three-by-three image.
    Parameters:
    -----------
    directory : The directory (str; with wildcards and extension) of the
                images to be plotted.
                E.g. 'my_coding_routines/images/test/*.png'
    nrow : The number of rows of images in the file.
    ncol : The number of columns of images in the file.
    title : (default = '')
            The title of the graph (str).  By default, none is added.
    """
    fig = plt.figure(facecolor='white') # removing 'facecolor' sets it to 'None'

    mainTitle = title
    fig.suptitle(mainTitle,fontsize = 18)

    fileList = glob.glob(directory)
    
    for i in range(1,(nrow*ncol)+1):
        axes = fig.add_subplot(nrow,ncol,i)
        img = mpimg.imread(fileList[i-1])
        imgplot = axes.imshow(img)
        axes.tick_params(
            axis='both',        # Apply to both x- and y-axes
            which='both',       # Turns major and minor ticks off
            left = 'off',       # Turns axis ticks off
            right = 'off',
            bottom='off',      
            top='off',         
            labelbottom='off',  # Turns axis labels off
            labelleft='off')
        if i == 1:
            axes.set_title('ENSO Positive')
            axes.set_ylabel('IPO Positive',fontsize=15)
            
        elif i == 2:
            axes.set_title('ENSO Neutral')
        elif i == 3:
            axes.set_title('ENSO Negative')
        elif i == 4:
            axes.set_ylabel('IPO Neutral',fontsize=15)
        elif i == 7:
            axes.set_ylabel('IPO Negative',fontsize=15)
        else:
            pass

    """
    #Code for colorbar - but will only go between 0 and 1.
    #If include, will need to add "units" to function arguments.
    #Will also need to make sure it is the right colour scheme.
    pylab.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    cax = pylab.axes([0.85, 0.1, 0.04, 0.8])
    pylab.colorbar(cax=cax,ticks=[0, 0.5, 1.5])
    """
    #pylab.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    #cax = pylab.axes([0.85, 0.1, 0.04, 0.8])
    #cbar = plt.colorbar(cax=cax)
    #cbarLabel = "%s" %(Dict['var_units'])
    #cbar.set_label(cbarLabel)
    
    return fig

AWAP_June = multi("my_coding_routines/images/composite/"+num+"/rainfall/AWAP/June/*.png",3,3,title='AWAP June: mean rainfall')
#AWAP_June_Anom = multi("my_coding_routines/images/composite/"+num+"/rainfall_anomalies/AWAP/June/*.png",3,3,title='AWAP June: mean rainfall anomalies')

plt.show()
#maps_sub.saveFig(AWAP_June,"","composite/"+num+"_compiled/AWAP/AWAP_June")
#maps_sub.saveFig(AWAP_June_Anom,"","composite/"+num+"_compiled/AWAP/AWAP_June_Anom")
