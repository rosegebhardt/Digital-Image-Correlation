import sys
import os
from os.path import abspath
sys.path.extend([abspath(".")])

import muDIC as dic
import logging
import numpy as np
import matplotlib as plt

# Run DIC algorithm
def run_DIC(folder_path,n_images,filter,filter_sigma,maxim,maxit,padding,poly_order,converge):

    # Set the amount of info printed to terminal during analysis
    logging.basicConfig(format='%(name)s:%(levelname)s:%(message)s', level=logging.INFO)

    # Path to folder containing images
    path = folder_path

    # Generate image instance containing all images found in the folder
    images = dic.IO.image_stack_from_folder(path, file_type='.png')
    images.use_every_n_image(int(n_images))
    if filter == "Lowpass Gaussian":
        images.set_filter(dic.filtering.lowpass_gaussian, sigma=int(filter_sigma))
    elif filter == "Highpass Gaussian":
        images.set_filter(dic.filtering.highpass_gaussian, sigma=int(filter_sigma))
    elif filter == "Homomorphic Median":
        images.set_filter(dic.filtering.homomorphic_median, sigma=int(filter_sigma))
    else:
        pass

    # Generate mesh
    mesher = dic.Mesher(deg_e=3, deg_n=3, type="q4")#type="b_splines")
    mesh = mesher.mesh(images,Xc1=316,Xc2=523,Yc1=209,Yc2=1055,n_ely=18,n_elx=5, GUI=True)

    # Instantiate settings object and set some settings manually (first video)
    settings = dic.DICInput(mesh, images)
    if bool(maxim):
        settings.max_nr_im = int(maxim)
    settings.ref_update = [15]
    settings.maxit = int(maxit) 
    settings.tol = 1.e-6
    settings.interpolation_order = int(poly_order)

    # If you want to access the residual fields after the analysis, this should be set to True
    settings.store_internals = True

    # This setting defines the behaviour when convergence is not obtained
    if converge == "Ignore":
        settings.noconvergence = "ignore"
    elif converge == "Update":
        settings.noconvergence = "update"
    elif converge == "Break":
        settings.noconvergence = "break"
    else:
        pass

    # Instantiate job object
    job = dic.DICAnalysis(settings)

    # Running DIC analysis
    dic_results = job.run()

    return images, dic_results

# Display outputs on matplotlib
def show_fields(image_stack,dic_results,which_field,amount_upscale,comp):

    # Calculate field values
    fields = dic.post.viz.Fields(dic_results,upscale=int(amount_upscale))

    # Instantiate visualizer object
    viz = dic.Visualizer(fields,images=image_stack)

    # Show displacement field
    if which_field == "Displacement":
        viz.show(field="displacement", component = comp, frame=-1)

    elif which_field == "True Strain":
        viz.show(field="truestrain", component = comp, frame=-1)

    elif which_field == "Engineering Strain":
        viz.show(field="engstrain", component = comp, frame=-1)

    elif which_field == "Green Strain":
        viz.show(field="greenstrain", component = comp, frame=-1)

    elif which_field == "Residual":
        viz.show(field="residual", component = comp, frame=-1) 

    else:
        print("uh oh spaghettios...")

# Save output as CSV
def save_csv(dic_results,which_field,amount_upscale,comp,dir):

    # Directory where CSV is saved
    out_dir = os.path.expanduser(dir)

    # Calculate field values
    fields = dic.post.viz.Fields(dic_results,upscale=int(amount_upscale))

    # Save output as CSV
    if which_field == "Displacement":
        disp_data = fields.disp()[0, comp[0], :, :, -1]
        np.savetxt(os.path.join(out_dir,"displacement_data.csv"),disp_data,delimiter=",")

    elif which_field == "True Strain":
        true_strain_data = fields.true_strain()[0, comp[0], comp[1], :, :, -1]
        np.savetxt(os.path.join(out_dir,"true_strain_data.csv"),true_strain_data,delimiter=",")

    elif which_field == "Engineering Strain":
        eng_strain_data = fields.eng_strain()[0, comp[0], comp[1], :, :, -1]
        np.savetxt(os.path.join(out_dir,"eng_strain_data.csv"),eng_strain_data,delimiter=",")

    elif which_field == "Green Strain":
        green_strain_data = fields.green_strain()[0, comp[0], comp[1], :, :, -1]
        np.savetxt(os.path.join(out_dir,"green_strain_data.csv"),green_strain_data,delimiter=",")

    elif which_field == "Residual":
        residual_data = fields.residual(-1)
        np.savetxt(os.path.join(out_dir,"residual_data.csv"),residual_data,delimiter=",")

    else:
        print("uh oh spaghettios..") # make a better error statement


# Save output as NPY (numpy array)
def save_npy(dic_results,which_field,amount_upscale,comp,dir):

    # Directory where NPY is saved
    out_dir = os.path.expanduser(dir)

    # Calculate field values
    fields = dic.post.viz.Fields(dic_results,upscale=int(amount_upscale))

    # Save output as NPY
    if which_field == "Displacement":
        disp_data = fields.disp()[0, comp[0], :, :, -1]
        np.save(os.path.join(out_dir,"displacement_data.npy"),disp_data) 

    elif which_field == "True Strain":
        true_strain_data = fields.true_strain()[0, comp[0], comp[1], :, :, -1]
        np.save(os.path.join(out_dir,"true_strain_data.npy"),true_strain_data)

    elif which_field == "Engineering Strain":
        eng_strain_data = fields.eng_strain()[0, comp[0], comp[1], :, :, -1]
        np.save(os.path.join(out_dir,"eng_strain_data.npy"),eng_strain_data)

    elif which_field == "Green Strain":
        green_strain_data = fields.green_strain()[0, comp[0], comp[1], :, :, -1]
        np.save(os.path.join(out_dir,"green_strain_data.npy"),green_strain_data)

    elif which_field == "Residual":
        residual_data = fields.residual(-1)
        np.save(os.path.join(out_dir,"residual_data.npy"),residual_data)

    else:
        print("uh oh spaghettios...") # make a better error statement
