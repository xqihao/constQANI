import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from mpl_toolkits.axes_grid1 import make_axes_locatable


### --------------------------------------------
def plot_check_model(field, nz, nx):
    fig = plt.figure(figsize=(7, 7))
    fig.subplots_adjust(left=.20, bottom=.16, right=.99, top=.97)

    ax = plt.gca()
    ##im = plt.imshow(field, extent=[0,(nx-1)*dx,(nz-1)*dz,0], aspect=(nx-1)*dx/(nz-1)/dz, cmap="jet")
    im = plt.imshow(field, aspect=1, cmap="jet")    

    plt.colorbar(im, orientation="horizontal")
#     plt.colorbar(im, location='bottom', shrink=0.8*nz/nx)
    
    plt.show()
    plt.close()
### --------------------------------------------
def plot_snapshot(title,filename,field, nz, nx, dz, dx, zlab, xlab, asp=1, clip=0.001, color="jet"):
    """ plot snapshot  """
    plt.figure(figsize=(7,4))
    fig = plt.subplots_adjust(left=0.15, bottom=0.1, top=0.95, right=0.95)
    plt.title(title)
    plt.xlim(0, (nx-1)*dx)
    plt.ylim((nz-1)*dz, 0)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(zlab, fontsize=14)
    
    max_val = np.max(np.abs(field))
    
    image = plt.imshow(field,vmin=-max_val*clip,vmax=max_val*clip, \
                       extent=[0,(nx-1)*dx,(nz-1)*dz,0],aspect=asp,cmap=color)
    plt.colorbar(image,shrink=0.7)
    full_filename = './figs/'+filename + '.pdf'
    #plt.savefig(full_filename, dpi=800, bbox_inches="tight")
    plt.show()
    plt.close
### --------------------------------------------
def plot_data(title,filename,data, nt, nx, dt, dx, zlab, xlab, clip=1, asp=2, color='jet'):

    max_val = np.max(np.abs(data))
    tmp = np.clip(data,-clip*max_val,clip*max_val) # Clip and scale data at fraction of max
    plt.figure(figsize=(7,6))
    plt.subplots_adjust(left=0.1, bottom=0.1, top=0.9, right=0.9)
    image = plt.imshow(tmp,vmin=-max_val*clip,vmax=max_val*clip, \
                       extent=[0, (nx-1)*dx, (nt-1)*dt,0], aspect=asp, cmap=color)
    plt.title(title)
    plt.colorbar(image, shrink=1./asp)
    plt.xlim(0, (nx-1)*dx)
    plt.ylim((nt-1)*dt, 0)
    plt.xlabel(zlab, fontsize=14)
    plt.ylabel(xlab, fontsize=14)
    full_filename = './figs/'+filename + '.pdf'
    plt.savefig(full_filename, dpi=800, bbox_inches="tight")
    plt.show()
    plt.close()


