# -*- coding: utf-8 -*-
"""

"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def D(x,y):
    return (x*1e-9*y*1e-6)/4.3

def F(x,y):
    return (x*1e-9*y*1e-6)/6.4



x=np.linspace(10,382,545)
y=np.linspace(10,500,545)

x,y=np.meshgrid(x,y)
z=D(x,y)
Z=F(x,y)


fig = plt.figure(figsize=(15,10))
ax = plt.axes(projection='3d')
ax.tick_params(labelsize=16)
ax.contour3D(x,y,z, 100, cmap='winter')
ax.contour3D(x,y,Z,100,cmap='autumn')
#ax.plot_surface(x,y,z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
ax.set_xlabel(r'$\.E\ [\frac{nm}{s}]$',labelpad=12,fontsize=20)
ax.set_ylabel('$H_0\ [\mu m]$',labelpad=14, fontsize=20)
ax.zaxis.set_rotate_label(False) 
ax.set_zlabel(r'$D\ [\frac{m^2}{s}]$', rotation='vertical', labelpad=8, fontsize=20)

ax.text(0,450,0.39e-10, '$\Phi_S=0.15$', color='blue', fontsize=20)
ax.text(0,450,0.35e-10, '$\Phi_S=0.1$', color='red', fontsize=20)

ax.view_init(30,-45)
plt.show()

x=np.linspace(10,382,545)
plt.plot(x,(x*1e-9*500e-6)/4.3,'b-',label='$\Phi_S=0.15$')
plt.plot(x,(x*1e-9*500e-6)/6.4,'r-', label='$\Phi_S=0.1$')
plt.ylim(0,4e-11)
plt.tick_params(labelsize=14)
plt.legend(fontsize=14)
plt.xlabel(r'$\.E\ [\frac{nm}{s}]$',fontsize=14)
plt.ylabel(r'$D\ [\frac{m^2}{s}]$',fontsize=14)
plt.text(190,0.6e-11,r'$H_0=500\ [\mu m]$',fontsize=14)
plt.text(130,0.25e-11,r'$Pe\ chosen\ to\ satisfy\ Pe>\frac{0.64}{\Phi_S}$',fontsize=14)
plt.grid()
plt.show()

x=np.linspace(10,382,545)
plt.plot(x,(x*1e-9*150e-6)/4.3,'b-',label='$\Phi_S=0.15$')
plt.plot(x,(x*1e-9*150e-6)/6.4,'r-', label='$\Phi_S=0.1$')
plt.ylim(0,1.5e-11)
plt.tick_params(labelsize=14)
plt.legend(fontsize=14)
plt.xlabel(r'$\.E\ [\frac{nm}{s}]$',fontsize=14)
plt.ylabel(r'$D\ [\frac{m^2}{s}]$',fontsize=14)
plt.text(190,0.25e-11,r'$H_0=150\ [\mu m]$',fontsize=14)
plt.text(130,0.1e-11,r'$Pe\ chosen\ to\ satisfy\ Pe>\frac{0.64}{\Phi_S}$',fontsize=14)
plt.grid()
plt.show()
