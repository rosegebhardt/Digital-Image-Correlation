# This allows for running the example when the repo has been cloned
import sys
from os.path import abspath
sys.path.extend([abspath(".")])

import muDIC as dic
import logging
import matplotlib as plt

# Set the amount of info printed to terminal during analysis
logging.basicConfig(format='%(name)s:%(levelname)s:%(message)s', level=logging.INFO)

# Path to folder containing images
path = r'/home/rose/Desktop/muDIC/data/test_11/vid11_frames' # First video

# Generate image instance containing all images found in the folder
images = dic.IO.image_stack_from_folder(path, file_type='.png')
images.use_every_n_image(10)
images.set_filter(dic.filtering.lowpass_gaussian, sigma=1.)

# Generate mesh
mesher = dic.Mesher(deg_e=3, deg_n=3, type="q4")#type="b_splines")
mesh = mesher.mesh(images,Xc1=316,Xc2=523,Yc1=209,Yc2=1055,n_ely=18,n_elx=5, GUI=True)

# Instantiate settings object and set some settings manually (first video)
settings = dic.DICInput(mesh, images)
settings.max_nr_im = 300
settings.ref_update = [15]
settings.maxit = 20
settings.tol = 1.e-6
settings.interpolation_order = 4

# If you want to access the residual fields after the analysis, this should be set to True
settings.store_internals = True

# This setting defines the behaviour when convergence is not obtained
settings.noconvergence = "ignore"

# Instantiate job object
job = dic.DICAnalysis(settings)

# Running DIC analysis
dic_results = job.run()

# Calculate field values
fields = dic.post.viz.Fields(dic_results,upscale=15)

# Show displacement field
viz = dic.Visualizer(fields,images=images)
viz.show(field="displacement", component = (1,1), frame=-1)
viz.show(field="truestrain", component = (1,1), frame=-1)

