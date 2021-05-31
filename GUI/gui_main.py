import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import get_frames
import dic_main

COLUMN_1 = 0.05
COLUMN_2 = 0.30
COLUMN_3 = 0.55
COLUMN_4 = 0.80

TOP_OFFSET = 0.06
ROW_STEP1 = TOP_OFFSET+0.075
ROW_STEP2 = TOP_OFFSET+0.275
ROW_STEP3 = TOP_OFFSET+0.625

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.filename = None
        self.foldername = None
        # self.components = (1,1)
        self.master = master
        self.pack()
        self.upload_files()
        self.choose_settings()
        self.view_results()
        # # Can be used for making resizable background image - looks awful
        # self.bg_img = Image.open("dic-speckle.png")
        # self.bg_img_copy = self.bg_img.copy()
        # self.background_image = ImageTk.PhotoImage(self.bg_img)
        # self.background = tk.Label(self, image=self.background_image)
        # self.background.pack(fill=tk.BOTH, expand=True)
        # self.background.bind('<Configure>', self._resize_image)

    # def _resize_image(self,event):
    #     new_width = event.width
    #     new_height = event.height
    #     self.bg_img = self.bg_img_copy.resize((new_width, new_height))
    #     self.background_image = ImageTk.PhotoImage(self.bg_img)
    #     self.background.configure(image =  self.background_image)

    def error_popup(self,error_msg):
        win = tk.Toplevel()
        win.wm_title("Error Warning")
        warning = tk.Label(win, text=error_msg,font=main_font)
        warning.grid(row=0, column=0)
        dismiss = tk.Button(win, text="Okay", command=win.destroy)
        dismiss.grid(row=1, column=0)

    def upload(self,event=None):
        self.filename = filedialog.askopenfilename()
        if self.filename.endswith('.mp4'):
            print('File Selected: ', self.filename)
        else:
            self.error_popup('ERROR: Please upload an MP4 file.')
            self.filename = ""

    def choose_dir(self):
        self.foldername = filedialog.askdirectory()
        print('Directory Selected: ', self.foldername)

    def choose_stack_dir(self):
        self.foldername = filedialog.askdirectory()
        print('Image Stack Directory Selected: ', self.foldername)
        
    def video_to_images(self):
        if (self.filename is not None) and (self.foldername is not None):
            get_frames.mp4_frames(self.filename,self.foldername)
        else:
            self.error_popup('ERROR: Please choose a video file and output directory.')

    def get_comp(self):
        COMP = self.which_comp.get()
        print(COMP)
        if COMP == "XX":
            return (0,0)
        elif COMP == "XY":
            return (0,1)
        elif COMP == "YX":
            return (1,0)
        elif COMP == "YY":
            return (1,1)
        else:
            error_popup("uh oh spaghettios...")
     
    def runDIC(self):
        if self.foldername == None:
            self.error_popup("ERROR: Please choose an image stack.")
            return
        else:
            self.image_stack, self.dic_results = dic_main.run_DIC(self.foldername,
            self.nth_image.get(),
            self.filter.get(),
            self.sigma.get(),
            self.maxim.get(),
            self.maxit.get(),
            self.padding.get(),
            self.interp.get(),
            self.converge.get())
 
    def display_field(self):
        self.components = self.get_comp()
        try: self.image_stack
        except AttributeError: self.error_popup("ERROR: Please run DIC before displaying results.")
        else: dic_main.show_fields(self.image_stack,self.dic_results,self.which_field.get(),self.upscale.get(),self.components)

    def save_csv(self):
        self.get_comp
        try: self.dic_results
        except AttributeError: self.error_popup("ERROR: Please run DIC before saving results.")
        else: 
            self.csvfoldername = filedialog.askdirectory()
            dic_main.save_csv(self.dic_results,self.which_field.get(),self.upscale.get(),self.components,self.csvfoldername)

    def save_npy(self):
        sel.get_comp
        try: self.dic_results
        except AttributeError: self.error_popup("ERROR: Please run DIC before saving results.")
        else:
            self.npyfoldername = filedialog.askdirectory()
            dic_main.save_npy(self.dic_results,self.which_field.get(),self.upscale.get(),self.components,self.npyfoldername)
        
    #----------WIDGETS
    
    def upload_files(self):
        
        self.upload_label = tk.Label(root,text='Step 1a: Upload Files and Choose Directory',font=header_font)
        self.upload_label.pack()
        self.upload_label.place(relx=COLUMN_1, rely=ROW_STEP1, anchor=tk.W)

        self.upload_widget = tk.Button(root, text='Upload Video File', command=self.upload,
        bg='white',fg='black',font=main_font,height=1,width=20)
        self.upload_widget.pack()
        self.upload_widget.place(relx=COLUMN_1, rely=ROW_STEP1+0.05, anchor=tk.W)

        self.choose_dir_widget = tk.Button(root, text='Choose Output Directory', command=self.choose_dir,
        bg='white',fg='black',font=main_font,height=1,width=20)
        self.choose_dir_widget.pack()
        self.choose_dir_widget.place(relx=COLUMN_2, rely=ROW_STEP1+0.05, anchor=tk.W)

        self.video_to_images_widget = tk.Button(root, text='Get Image Stack', command=self.video_to_images,
        bg='white',fg='black',font=main_font,height=1,width=20)
        self.video_to_images_widget.pack()
        self.video_to_images_widget.place(relx=COLUMN_1, rely=ROW_STEP1+0.10, anchor=tk.W)
        
        self.imagestack_label = tk.Label(root,text='Step 1b: Choose Image Stack Directory',font=header_font)
        self.imagestack_label.pack()
        self.imagestack_label.place(relx=COLUMN_3, rely=ROW_STEP1, anchor=tk.W)

        self.upload_widget = tk.Button(root, text='Choose Image Stack Directory', command=self.choose_stack_dir,
        bg='white',fg='black',font=main_font,height=1,width=25)
        self.upload_widget.pack()
        self.upload_widget.place(relx=COLUMN_3, rely=ROW_STEP1+0.05, anchor=tk.W)


    def choose_settings(self):
        
        # Label Step 2
        self.settings_label = tk.Label(root,text='Step 2: Choose DIC Settings',font=header_font)
        self.settings_label.pack()
        self.settings_label.place(relx=COLUMN_1, rely=ROW_STEP2, anchor=tk.W)
        
        #----------IMAGE PARAMETERS
        
        # Choose filtering method
        FILTERS = ["None","Highpass Gaussian","Lowpass Gaussian","Homomorphic Median"]
        self.filter_label = tk.Label(root,text='Image Filter Type:',font=main_font)
        self.filter_label.pack()
        self.filter_label.place(relx=COLUMN_1, rely=ROW_STEP2+0.05, anchor=tk.W)
        self.filter = tk.StringVar(root)
        self.filter.set(FILTERS[0]) # default value
        self.filters = tk.OptionMenu(root,self.filter,*FILTERS)
        self.filters.config(font=main_font)
        self.filters.pack()
        self.filters.place(relx=COLUMN_2, rely=ROW_STEP2+0.05, anchor=tk.W)
        
        # Choose strength of filter
        self.sigma = tk.StringVar(root)
        self.sigma.set("1.0")
        self.sigma_label = tk.Label(root,text='Filter Strength (Sigma):',font=main_font)
        self.sigma_label.pack()
        self.sigma_label.place(relx=COLUMN_1, rely=ROW_STEP2+0.10, anchor=tk.W)
        self.sigma_entry = tk.Entry(root,textvariable=self.sigma,font=main_font)
        self.sigma_entry.pack()
        self.sigma_entry.place(relx=COLUMN_2, rely=ROW_STEP2+0.10, anchor=tk.W)

        # Choose every nth image
        self.nth_image = tk.StringVar(root)
        self.nth_image.set("10")
        self.nth_image_label = tk.Label(root,text='Use Every Nth Image:',font=main_font)
        self.nth_image_label.pack()
        self.nth_image_label.place(relx=COLUMN_1, rely=ROW_STEP2+0.15, anchor=tk.W)
        self.nth_image_entry = tk.Entry(root,textvariable=self.nth_image,font=main_font)
        self.nth_image_entry.pack()
        self.nth_image_entry.place(relx=COLUMN_2, rely=ROW_STEP2+0.15, anchor=tk.W)
        
        # Choose maximum number of images to be proccessed
        self.maxim = tk.StringVar(root)
        self.maxim.set("")
        self.maxim_label = tk.Label(root,text='Maximum Images (Optional):',font=main_font)
        self.maxim_label.pack()
        self.maxim_label.place(relx=COLUMN_1, rely=ROW_STEP2+0.20, anchor=tk.W)
        self.maxim_entry = tk.Entry(root,textvariable=self.maxim,font=main_font)
        self.maxim_entry.pack()
        self.maxim_entry.place(relx=COLUMN_2, rely=ROW_STEP2+0.20, anchor=tk.W)
        
        #----------CORRELATION PARAMETERS
                
        # Choose maximum number of iterations
        self.maxit = tk.StringVar(root)
        self.maxit.set("40")
        self.maxit_label = tk.Label(root,text='Maximum Iterations:',font=main_font)
        self.maxit_label.pack()
        self.maxit_label.place(relx=COLUMN_3, rely=ROW_STEP2+0.05, anchor=tk.W)
        self.maxit_entry = tk.Entry(root,textvariable=self.maxit,font=main_font)
        self.maxit_entry.pack()
        self.maxit_entry.place(relx=COLUMN_4, rely=ROW_STEP2+0.05, anchor=tk.W)

        # Padding around mesh
        self.padding = tk.StringVar(root)
        self.padding.set("10")
        self.padding_label = tk.Label(root,text='Padding Around Mesh (Pixels):',font=main_font)
        self.padding_label.pack()
        self.padding_label.place(relx=COLUMN_3, rely=ROW_STEP2+0.10, anchor=tk.W)
        self.padding_entry = tk.Entry(root,textvariable=self.padding,font=main_font)
        self.padding_entry.pack()
        self.padding_entry.place(relx=COLUMN_4, rely=ROW_STEP2+0.10, anchor=tk.W)
        
        # Interpolation Polynomial Order
        self.interp = tk.StringVar(root)
        self.interp.set("3")
        self.interp_label = tk.Label(root,text='Interpolation Polynomial Order: ',font=main_font)
        self.interp_label.pack()
        self.interp_label.place(relx=COLUMN_3, rely=ROW_STEP2+0.15, anchor=tk.W)
        self.interp_entry = tk.Entry(root,textvariable=self.interp,font=main_font)
        self.interp_entry.pack()
        self.interp_entry.place(relx=COLUMN_4, rely=ROW_STEP2+0.15, anchor=tk.W)
        
        # No Convergence
        NO_CONVERGENCE = ["Ignore","Update","Break"]
        self.converge_label = tk.Label(root,text='If Convergence Fails: ',font=main_font)
        self.converge_label.pack()
        self.converge_label.place(relx=COLUMN_3, rely=ROW_STEP2+0.20, anchor=tk.W)
        self.converge = tk.StringVar(root)
        self.converge.set(NO_CONVERGENCE[0]) # default value
        self.convergence = tk.OptionMenu(root,self.converge,*NO_CONVERGENCE)
        self.convergence.config(font=main_font)
        self.convergence.pack()
        self.convergence.place(relx=COLUMN_4, rely=ROW_STEP2+0.20, anchor=tk.W)
        
        # Run DIC Algorithm
        self.runDIC_widget = tk.Button(root, text='Run Digital Image Correlation', command=self.runDIC,
        bg='white',fg='black',font=main_font,height=1,width=25)
        self.runDIC_widget.pack()
        self.runDIC_widget.place(relx=COLUMN_1, rely=ROW_STEP2+0.25, anchor=tk.W)

    def view_results(self):
        
        # Label Step 3
        self.results_label = tk.Label(root,text='Step 3: View Results',font=header_font)
        self.results_label.pack()
        self.results_label.place(relx=COLUMN_1, rely=ROW_STEP3, anchor=tk.W)
 
        # Choose strength of filter
        self.upscale = tk.StringVar(root)
        self.upscale.set("10")
        self.upscale_label = tk.Label(root,text='Upscale:',font=main_font)
        self.upscale_label.pack()
        self.upscale_label.place(relx=COLUMN_3, rely=ROW_STEP3+0.05, anchor=tk.W)
        self.upscale_entry = tk.Entry(root,textvariable=self.upscale,font=main_font)
        self.upscale_entry.pack()
        self.upscale_entry.place(relx=COLUMN_4, rely=ROW_STEP3+0.05, anchor=tk.W)
        
        # Choose filtering method
        FIELDS = ["Displacement","True Strain","Engineering Strain",
                  "Green Strain","Residual"]
        self.field_label = tk.Label(root,text='Choose Field:',font=main_font)
        self.field_label.pack()
        self.field_label.place(relx=COLUMN_1, rely=ROW_STEP3+0.05, anchor=tk.W)
        self.which_field = tk.StringVar(root)
        self.which_field.set(FIELDS[0]) # default value
        self.field = tk.OptionMenu(root,self.which_field,*FIELDS)
        self.field.config(font=main_font)
        self.field.pack()
        self.field.place(relx=COLUMN_2, rely=ROW_STEP3+0.05, anchor=tk.W)

        # Choose component to display
        COMPONENTS = ["XX","XY","YX","YY"]
        self.comp_label = tk.Label(root,text='Choose Field:',font=main_font)
        self.comp_label.pack()
        self.comp_label.place(relx=COLUMN_1, rely=ROW_STEP3+0.10, anchor=tk.W)
        self.which_comp = tk.StringVar(root)
        self.which_comp.set(COMPONENTS[3]) # default value
        self.comp = tk.OptionMenu(root,self.which_comp,*COMPONENTS)
        self.comp.config(font=main_font)
        self.comp.pack()
        self.comp.place(relx=COLUMN_2, rely=ROW_STEP3+0.10, anchor=tk.W)
               
        # View Fields
        self.disp_field_widget = tk.Button(root, text='Display Field', command=self.display_field,
        bg='white',fg='black',font=main_font,height=1,width=25)
        self.disp_field_widget.pack()
        self.disp_field_widget.place(relx=COLUMN_1, rely=ROW_STEP3+0.16, anchor=tk.W)
        
        # Save Output as CSV
        self.save_csv_widget = tk.Button(root, text='Save Output as .CSV', command=self.save_csv,
        bg='white',fg='black',font=main_font,height=1,width=25)
        self.save_csv_widget.pack()
        self.save_csv_widget.place(relx=COLUMN_2, rely=ROW_STEP3+0.16, anchor=tk.W)
        
        # Save Output as NPY
        self.save_npy_widget = tk.Button(root, text='Save Output as .NPY', command=self.save_npy,
        bg='white',fg='black',font=main_font,height=1,width=25)
        self.save_npy_widget.pack()
        self.save_npy_widget.place(relx=COLUMN_3, rely=ROW_STEP3+0.16, anchor=tk.W)

      
root = tk.Tk()
root.wm_title("Digital Image Correlation GUI")
root.geometry("2000x1200")

main_font = tkFont.Font(family="Helvetica",size=10,weight="bold")
header_font = tkFont.Font(family="Helvetica",size=12,weight="bold")

# root.configure(background='grey')

app = Application(master=root)

root.mainloop()
app.mainloop()