from nibabel import load
from nipy.labs.viz import cm
from nipy.labs import viz3d

# take a statsitics to visualize
brain_map = load('spmT_0029.nii.gz')
# value range
vmin, vmax = brain_map.get_data().min(), brain_map.get_data().max()

viz3d.plot_map_3d(brain_map.get_data(), 
                  brain_map.get_affine(),
                  cmap=cm.cold_hot,
                  vmin=vmin,
                  vmax=vmax,
                  anat=None,
                  threshold=4)



