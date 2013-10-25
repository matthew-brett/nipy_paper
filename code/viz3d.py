#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
from __future__ import print_function
__doc__ = """
This examples performs sifferent kinds of (2D and 3D) plots
of a given activation map.

Needs matplotlib.

Author : Bertrand Thirion, 2012
"""
print(__doc__)

from os import path
import matplotlib.pyplot as plt
from nibabel import load
from nipy.labs.viz import plot_map, cm
from nipy.labs import viz3d
from mayavi import mlab

# Local import
from get_data_light import DATA_DIR, get_second_level_dataset

#######################################
# Data and analysis parameters
#######################################

input_image = path.join(DATA_DIR, 'spmT_0029.nii.gz')
if not path.exists(input_image):
    get_second_level_dataset()

brain_map = load(input_image)
vmin, vmax = brain_map.get_data().min(), brain_map.get_data().max()

viz3d.plot_map_3d(brain_map.get_data(), brain_map.get_affine(),
                  cmap=cm.cold_hot,
                  vmin=vmin,
                  vmax=vmax,
                  anat=None,
                  threshold=4)
mlab.savefig('viz_3d.png')


