from nipy import load_image
from nipy.algorithms.registration import (HistogramRegistration,
                                          Affine,
                                          resample)

# Load input images
fmri_img = load_image('mean_fmri.nii')
t1_img = load_image('T1.nii')

# First pass: rigid registration using mutual information
reg = HistogramRegistration(fmri_img, t1_img, similarity='mi')
T = reg.optimize('rigid')

# Second pass: 12-parameter affine registration using a custom variant
# of mutual information based on the Hellinger distance
def mymi(H):
    # takes a 2D array representing the joint histogram as input
    P = H / H.sum()
    Pi = P.sum(0).reshape((H.shape[1], 1))
    Pj = P.sum(1).reshape((H.shape[0], 1))
    return np.sum((np.sqrt(P) - np.sqrt(Pi.T * Pj)) ** 2)

T2 = Affine(T.as_affine())
reg2 = HistogramRegistration(fmri_img, t1_img, similarity=mymi)
T2 = reg2.optimize(T2)

# Resample the fMRI image in T1 space
reg_fmri_img = resample(fmri_img, T2.inv(), reference=t1_img)
