# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:20:59 2018

@author: ms01106
"""


import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import matplotlib.cm
import numpy as np
from pylab import meshgrid
import matplotlib.mlab as mlab

# setup files etc
data_dir = "//surrey.ac.uk/Research/Malin_Schulz_PhDproject/Experimental/Raman/22AY04/20180424/txt files/Phygly_on_Sty-BA-AA_457_static_50%_depth_5um/"
data_file_count = int(len(os.listdir(data_dir))) 
filename_pattern = data_dir+"Phygly_on_Sty-BA-AA_457_static_50%_depth_5um_Acq{0}.txt"

#data acquisition

waves = np.loadtxt(filename_pattern.format(1)).T[1]
ids = np.arange(1,data_file_count+1)
intensities = np.array([np.loadtxt(filename_pattern.format(i)).T[2] for i in ids])

#plotting

from matplotlib.ticker import AutoMinorLocator, MultipleLocator
fig = plt.figure(figsize=(15,10))
ax = fig.gca()
p = ax.pcolor(waves, range(0,data_file_count+1), intensities, cmap=matplotlib.cm.YlGnBu_r, vmin=intensities.min(), vmax=np.median(intensities.max(axis=1)))
cb = fig.colorbar(p, ax=ax)
cb.set_label("Intensity", fontsize=22)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=22)
plt.rc('legend', fontsize=20)
#ax.set_title("Raman 09.01.2018")
ax.set_xlabel("Wavenumber $[cm^{-1}]$")
ax.set_ylabel("Scan number")

ax.yaxis.set(ticks=np.arange(0.5, data_file_count, 2), ticklabels=ids[::2])
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

ax.xaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(200))
ax.axis([waves.min(), waves.max(), 0, data_file_count])
plt.arrow(393, 25, 1720,0, linestyle='--', ec='w',zorder=2)
plt.arrow(393,8, 1720,0, linestyle='--', ec='w',zorder=2)
plt.text(400, 0.2, r'film surface', fontsize=18, color='w')
plt.text(400, 30, r'150$\mu$m into the film', fontsize=18, color='w')
plt.text(1630, 2, r'Phytoglycogen layer', fontsize=18, color='w')
plt.text(1740, 8.5, r'Sty-BA-AA layer', fontsize=18, color='w')
plt.text(1750, 25.5, r'glass substrate', fontsize=18, color='w')
plt.savefig("//surrey.ac.uk/Research/Malin_Schulz_PhDproject/Experimental/Raman/22AY04/20180424/figures/Phygly_on_Sty-BA-AA_457_static_50%_depth_5um_contourmap.svg", transparent= True )
plt.show()