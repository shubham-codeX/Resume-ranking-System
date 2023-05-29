from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import shutil

def display(file, path):
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Bosch")
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading', background="lightgreen", foreground="grey")


    def enter_location(file, destination_folder):
        src = path + "/"
        dest_folder = destination_folder + "/"
    #         dict=print_lr()
        dir_list = []

        for i in file: #image_list
            shutil.copyfile(src + i, dest_folder + i)
        return 0

    def browse(pathvar):
        dirname = filedialog.askdirectory()
        pathvar.set(dirname)


    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=50)

    selected_items_list = []

    tree.column("# 1", anchor='center', width=80)
    tree.heading("# 1", text="Index")
    tree.column("# 2", anchor='center', width=400)
    tree.heading("# 2", text="Resume")
    tree.column("# 3", anchor='center')
    tree.heading("# 3", text="Matching %")
            
    tree.tag_configure('oddrow', background='#E5E4E2')
    tree.tag_configure('evenrow', background='white')
    for i in range(len(file)):
        if(i%2==0):
            tree.insert('', 'end', iid=i, values=(i+1 , file[i][0], file[i][1]), tags = ('oddrow',), text=(file[i][0]))
        else:
            tree.insert('', 'end', iid=i, values=(i+1, file[i][0], file[i][1]), tags = ('evenrow',), text=(file[i][0]))

    #---------------------------------------------Frame creation ----------------------------------------------------------------
    frame=tk.Frame(root)
    frame.pack(side='top', anchor='n')
    frame1=tk.Frame(root)
    frame1.pack(side='top', anchor='n', pady=20)
    #------------------------------------------- destination ----------------------------------------------------------------------
    dest = tk.StringVar()
    destination_folder = tk.StringVar(value='')
    submit = tk.Button(frame1, text="Browse", width=10, command=lambda:browse(destination_folder))
    dest_browse = tk.Entry(frame1, width=51, text = destination_folder)
        
    dest_browse.pack(side='left', padx=5)
    submit.pack(side='left', padx=15)
        
    def dest_folder_location():
        return destination_folder.get()


    # ----------------------------------------- Required resume boxes -----------------------------------------------------------
    data = tk.IntVar()
    s_box =tk.Entry(frame, textvariable = data, width=5)
    s_len = tk.Label(frame, text= "/  " + str(len(file)), font=("Arial", 12))
    s_box.pack(side='left', padx=5)
    s_len.pack(side='left', padx=5)
    def print_lr():
        sb = int(s_box.get())
        for i in range(sb):
            selected_items_list.append(tree.item(i)['text'])
    #         print(selected_items_list)
        return selected_items_list

    btn = tk.Button(frame, text='Retrieve Resume', command=lambda : enter_location(print_lr(), dest_folder_location() ))
    btn.pack(side='left', padx=10)
    tree.pack(side='bottom', pady=20)
    root.mainloop()