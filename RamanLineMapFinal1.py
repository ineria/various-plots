# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:35:26 2018


"""

import os
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import glob


# setup files etc
data_dir = "//data/"
data_file_count = int(len(os.listdir(data_dir))+1) # +1 later!
data_files =sorted(glob.glob(data_dir+'name_Acq*'))

# 3d plotting

fig = plt.figure(figsize=(15,10))
ax = fig.gca(projection='3d')


for i,filename in enumerate(data_files):
    color =  matplotlib.cm.get_cmap('tab20b_r')(i/data_file_count)
    wave, intensity = np.loadtxt(filename).T[[2,3]]
    plt.plot(wave, wave*0-i/1, intensity.clip(0,700000), color = color)


##making graph pretty

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=22)
plt.rc('legend', fontsize=20)
ax.set_xlabel('Wavenumber $[cm^{-1}]$', labelpad=20)
ax.set_xlim3d(393, 2117)
ax.set_yticklabels([])
ax.set_zlabel('Intensity [a.u.]', labelpad=50)
#ax.set_zlim3d(4000,15000)
ax.tick_params(axis='z', pad=25)
ax.view_init(20, -70)
plt.savefig(data_dir+"image_linemap.svg", transparent= True )
plt.show()
