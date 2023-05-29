from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import glob
import os
import comparator as cm
import display
from tkinter import ttk
import read_files as rd
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry("900x600")

        self.master.title("Bosch")
        self.master.iconbitmap(r"logo.ico")

        #define raw buttons
        self.blank = tk.Label(self.master, text=" ")
        self.blank.grid(column=0, row=2)
        self.blank_1 = tk.Label(self.master, text=" ")
        self.blank_1.grid(column=0, row=3)

        #DEFINE BUTTONS AND LABELS
            #decription
        self.src = tk.Label(self.master, text="Job Description :", font=("Arial", 12))
        self.src.grid(column=0, row=3, sticky="W", padx=(50,0))

        desc_job=tk.StringVar()
        desc_path=tk.StringVar(value='')
        self.src_box = tk.Button(self.master, textvariable=desc_job, font=("Arial"), bg="#625D5D", fg="white", height=1, width=7, command=lambda:browse_file(desc_path))   #text-box to add job descrition
        desc_job.set("Browse")
        self.src_box.grid(column=0, row=3,sticky="W", pady=(0,0), padx=(690,0))

        desc_browse = tk.Entry(self.master, width=51, textvariable=desc_path)
        desc_browse.grid(row=3, column=0, padx=(350,0),sticky="w", pady=(0,0))



        # Source folder location and browsing
        self.src_1 = tk.Label(self.master, text="Enter Target Folder location :",font=("Arial", 12))
        self.src_1.grid(column=0, row=5, sticky="W", padx=(50,0), pady=(30,0))

        desc = tk.StringVar()
        src_path = tk.StringVar(value='')
        self.submit = tk.Button(self.master, textvariable=desc, font=("Arial"), bg="#625D5D", fg="white", height=1, width=7, command=lambda:browse(src_path))
        desc.set("Browse")
        self.submit.grid(column=0, row=5,sticky="W", pady=(30,0), padx=(690,0))

        txt_browse = tk.Entry(self.master, width=51, textvariable=src_path)
        txt_browse.grid(row=5, column=0, padx=(350,0),sticky="w", pady=(30,0))

        def file_location(self):
            return src_path.get()

        #funtion to retieve the input data

        def retrieveData(self):
            job_desc = desc_path.get()
            file_location = src_path.get()
            value = cm.output(file_location, job_desc)
            return value

        def return_data(self):
            value = retrieveData(self)
            dict={}
            keys=[]
            dir_list=[]
            os.chdir(file_location(self))
            for file in glob.glob("*.pdf"):
                keys.append(file)
            for file in glob.glob("*.docx"):
                keys.append(file)
            for file in glob.glob("*.doc"):
                keys.append(file)

            for i in range(len(keys)):
                dict[keys[i]] = value[i]
            dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
            return dict

        #OUTPUT BUTTON
        out_put=tk.StringVar()
        result = tk.Button(self.master, textvariable=out_put, font=("Arial"), bg="#DC143C", fg="white", height=1, width=10, command=lambda:display.display(return_data(self),file_location(self)))
        out_put.set("Sortlist")
        result.grid(column=0, row=7,pady=(80,0), sticky="w", padx=(330,0))

def browse(pathvar):
    dirname = filedialog.askdirectory()
    pathvar.set(dirname)
def browse_file(pathvar):
    dirname = filedialog.askopenfilename()
    pathvar.set(dirname)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bosch")
    root.iconbitmap(r"logo.ico")
    logo=Image.open("logo.png")
    logo=logo.resize((300, 100))
    logo=ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=1,padx=(21,0), pady=(10,0))
    App = ParentWindow(root)
    root.mainloop()