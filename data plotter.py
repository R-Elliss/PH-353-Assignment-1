import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages

dimensions=np.loadtxt("dimensions1to10.txt",delimiter=' ')
radii=np.loadtxt("radii1to5.txt",delimiter=' ')


with PdfPages('volume plots for varied radius and dimensions.pdf') as export_pdf:
    plt.subplot(1,2,1)
    plt.errorbar(radii[:,0],radii[:,1],yerr=radii[:,2],ecolor='red',elinewidth=2, capsize=3,marker='o',markersize=2,linestyle='none')
    plt.title('radii plot')
    plt.xlabel('radius')
    plt.ylabel('volume')
    plt.subplot(1,2,2)
    plt.errorbar(dimensions[:,0],dimensions[:,1],yerr=dimensions[:,2],ecolor='red',elinewidth=2, capsize=3, marker='o',markersize=2,linestyle='none')
    plt.xlabel('dimensions')
    plt.ylabel('volume')
    plt.title('dimensions plot')
    
    plt.tight_layout(4)
    export_pdf.savefig()