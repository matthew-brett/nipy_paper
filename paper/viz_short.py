from nibabel import load
from nipy.labs import viz

# activation image to look at
img = load('spmT_0029.nii.gz')
data = img.get_data()
affine = img.get_affine()
# visualize the activation on top of MNI template
viz.plot_map(data, affine, 
             cut_coords=(-52, 10, 22),
             threshold=3.0, 
             cmap=viz.cm.cold_hot)
plt.show()
