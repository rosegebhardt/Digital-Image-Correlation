import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import get_frames

class UploadFiles(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.mCan = tk.Canvas(self, height=1000, width=1000, bg='white')
        #self.mCan.pack()
        self.filename = None
        self.foldername = None
        self.master = master
        self.pack()
        self.create_widgets()

    def upload(self,event=None):
        self.filename = filedialog.askopenfilename()
        if self.filename.endswith('.mp4'):
            print('File Selected: ', self.filename)
        else:
            print('ERROR: Please upload an MP4 file.')
            self.filename = ""

    def choose_dir(self):
        self.foldername = filedialog.askdirectory()
        print('Directory Selected: ', self.foldername)

    def create_widgets(self):

        self.upload_widget = tk.Button(root, text='Upload Video File', command=self.upload,
        bg='white',fg='black',font=mono24,height=5,width=25)
        self.upload_widget.pack()
        self.upload_widget.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.choose_dir_widget = tk.Button(root, text='Choose Output Directory', command=self.choose_dir,
        bg='white',fg='black',font=mono24,height=5,width=25)
        self.choose_dir_widget.pack()
        self.choose_dir_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.video_to_images_widget = tk.Button(root, text='Get Image Stack', command=self.video_to_images,
        bg='white',fg='black',font=mono24,height=5,width=25)
        self.video_to_images_widget.pack()
        self.video_to_images_widget.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.pack(side="bottom")
       
    def video_to_images(self):
        if (self.filename is not None) and (self.foldername is not None):
            get_frames.mp4_frames(self.filename,self.foldername)
        else:
            print('Please choose filename and output directory')


root = tk.Tk()
root.geometry("800x800")

mono24 = tkFont.Font(family="monospace",size=24,weight="bold")

#bg = tk.PhotoImage(file = "bkg.png") 
#bg_label = tk.Label( root, image = bg) 
#bg_label.place(x = 0,y = 0) 

root.configure(background='grey')

app = UploadFiles(master=root)

root.mainloop()
app.mainloop()