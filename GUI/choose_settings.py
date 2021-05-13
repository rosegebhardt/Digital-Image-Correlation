import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ChooseSettings(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.mCan = tk.Canvas(self, height=1000, width=1000, bg='white')
        #self.mCan.pack()
        self.filename = None
        self.foldername = None
        self.master = master
        self.pack()
        self.create_widgets()

#    def upload(self,event=None):
#        self.filename = filedialog.askopenfilename()
#        if self.filename.endswith('.mp4'):
#            print('File Selected: ', self.filename)
#        else:
#            print('ERROR: Please upload an MP4 file.')
#            self.filename = ""
#
#    def choose_dir(self):
#        self.foldername = filedialog.askdirectory()
#        print('Directory Selected: ', self.foldername)

    def create_widgets(self):
        
        # Choose filtering method
        FILTERS = ["None","Highpass Gaussian","Lowpass Gaussian","Homomorphic Median"]
        self.filter_label = tk.Label(root,text='Image Filter Type: ',font=mono24)
        self.filter_label.pack()
        self.filter_label.place(relx=0.25, rely=0.15, anchor=tk.CENTER)
        self.filter = tk.StringVar(root)
        self.filter.set(FILTERS[0]) # default value
        self.filters = tk.OptionMenu(root,self.filter,*FILTERS)
        self.filters.config(font=mono24)
        self.filters.pack()
        self.filters.place(relx=0.75, rely=0.15, anchor=tk.CENTER)
        
        # Choose strength of filter
        self.sigma = tk.StringVar(root)
        self.sigma.set("1.0")
        self.sigma_label = tk.Label(root,text='Filter Strength (Sigma): ',font=mono24)
        self.sigma_label.pack()
        self.sigma_label.place(relx=0.25, rely=0.25, anchor=tk.CENTER)
        self.sigma_entry = tk.Entry(root,textvariable=self.sigma,font=mono24)
        self.sigma_entry.pack()
        self.sigma_entry.place(relx=0.75, rely=0.25, anchor=tk.CENTER)

        # Choose maximum number of iterations
        self.maxit = tk.StringVar(root)
        self.maxit.set("40")
        self.maxit_label = tk.Label(root,text='Maximum Number of Iterations: ',font=mono24)
        self.maxit_label.pack()
        self.maxit_label.place(relx=0.25, rely=0.35, anchor=tk.CENTER)
        self.maxit_entry = tk.Entry(root,textvariable=self.maxit,font=mono24)
        self.maxit_entry.pack()
        self.maxit_entry.place(relx=0.75, rely=0.35, anchor=tk.CENTER)
        
        # Choose maximum number of images to be proccessed
        self.maxim = tk.StringVar(root)
        self.maxim.set("")
        self.maxim_label = tk.Label(root,text='Maximum Images (Optional): ',font=mono24)
        self.maxim_label.pack()
        self.maxim_label.place(relx=0.25, rely=0.45, anchor=tk.CENTER)
        self.maxim_entry = tk.Entry(root,textvariable=self.maxim,font=mono24)
        self.maxim_entry.pack()
        self.maxim_entry.place(relx=0.75, rely=0.45, anchor=tk.CENTER)
        
        # Padding around mesh
        self.padding = tk.StringVar(root)
        self.padding.set("10")
        self.padding_label = tk.Label(root,text='Padding Around Mesh (Pixels): ',font=mono24)
        self.padding_label.pack()
        self.padding_label.place(relx=0.25, rely=0.55, anchor=tk.CENTER)
        self.padding_entry = tk.Entry(root,textvariable=self.padding,font=mono24)
        self.padding_entry.pack()
        self.padding_entry.place(relx=0.75, rely=0.55, anchor=tk.CENTER)
        
        # Store internals
        STORE = ["True","False"]
        self.store_label = tk.Label(root,text='Store Results: ',font=mono24)
        self.store_label.pack()
        self.store_label.place(relx=0.25, rely=0.65, anchor=tk.CENTER)
        self.store = tk.StringVar(root)
        self.store.set(STORE[0]) # default value
        self.stores = tk.OptionMenu(root,self.store,*STORE)
        self.stores.config(font=mono24)
        self.stores.pack()
        self.stores.place(relx=0.75, rely=0.65, anchor=tk.CENTER)
        
        # Interpolation Polynomial Order
        self.interp = tk.StringVar(root)
        self.interp.set("3")
        self.interp_label = tk.Label(root,text='Interpolation Polynomial Order: ',font=mono24)
        self.interp_label.pack()
        self.interp_label.place(relx=0.25, rely=0.75, anchor=tk.CENTER)
        self.interp_entry = tk.Entry(root,textvariable=self.interp,font=mono24)
        self.interp_entry.pack()
        self.interp_entry.place(relx=0.75, rely=0.75, anchor=tk.CENTER)
        
        # No Convergence
        NO_CONVERGENCE = ["Ignore","Update","Break"]
        self.converge_label = tk.Label(root,text='If Convergence Fails: ',font=mono24)
        self.converge_label.pack()
        self.converge_label.place(relx=0.25, rely=0.85, anchor=tk.CENTER)
        self.converge = tk.StringVar(root)
        self.converge.set(NO_CONVERGENCE[0]) # default value
        self.convergence = tk.OptionMenu(root,self.converge,*NO_CONVERGENCE)
        self.convergence.config(font=mono24)
        self.convergence.pack()
        self.convergence.place(relx=0.75, rely=0.85, anchor=tk.CENTER)
        
#        self.upload_widget = tk.Button(root, text='Upload Video File', command=self.upload,
#        bg='white',fg='black',font=mono24,height=5,width=25)
#        self.upload_widget.pack()
#        self.upload_widget.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
#
#        self.choose_dir_widget = tk.Button(root, text='Choose Output Directory', command=self.choose_dir,
#        bg='white',fg='black',font=mono24,height=5,width=25)
#        self.choose_dir_widget.pack()
#        self.choose_dir_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#
#        self.video_to_images_widget = tk.Button(root, text='Get Image Stack', command=self.video_to_images,
#        bg='white',fg='black',font=mono24,height=5,width=25)
#        self.video_to_images_widget.pack()
#        self.video_to_images_widget.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.pack(side="bottom")
       
#    def video_to_images(self):
#        if (self.filename is not None) and (self.foldername is not None):
#            get_frames.mp4_frames(self.filename,self.foldername)
#        else:
#            print('Please choose filename and output directory')


root = tk.Tk()
root.geometry("800x800")

mono24 = tkFont.Font(family="monospace",size=18,weight="bold")

#bg = tk.PhotoImage(file = "bkg.png") 
#bg_label = tk.Label( root, image = bg) 
#bg_label.place(x = 0,y = 0) 

root.configure(background='grey')

app = ChooseSettings(master=root)

root.mainloop()
app.mainloop()