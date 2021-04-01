import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import get_frames



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)
       
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
        bg='white',fg='black',height=5,width=25)
        self.upload_widget.pack()
        self.upload_widget.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.choose_dir_widget = tk.Button(root, text='Choose Output Directory', command=self.choose_dir,
        bg='white',fg='black',height=5,width=25)
        self.choose_dir_widget.pack()
        self.choose_dir_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.video_to_images_widget = tk.Button(root, text='Get Image Stack', command=self.video_to_images,
        bg='white',fg='black',height=5,width=25)
        self.video_to_images_widget.pack()
        self.video_to_images_widget.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.pack(side="bottom")
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()