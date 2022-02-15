"""
 - Create UI that allows:
    - Users to browse and choose source folder
    - Users to browse and choose destication folder
    - Manual 'File Check' process button
"""
#Importing necessary modules
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog as fd
import os
import shutil
import time

#Build out UI
class mainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("File Transfer")
        
        
        #GUI - Buttons
        self.btn_browse = tk.Button(self.master,width=15, height=1, text="Choose Source", command=lambda: browse_source(self))
        self.btn_browse.grid(row=0,column=0,padx=(15,0),pady=(35,5),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15, height=1, text="Choose Destination", command=lambda: browse_dest(self))
        self.btn_browse2.grid(row=1,column=0,padx=(15,0),pady=(5,5),sticky=W)
        self.btn_check = tk.Button(self.master,width=15, height=2, text="Transfer Files", command=lambda: transfer())
        self.btn_check.grid(row=2,column=0,padx=(15,0),pady=(5,5),sticky=W)
        self.btn_close = tk.Button(self.master,width=15, height=2, text="Close Program", command=lambda: ask_quit(self))
        self.btn_close.grid(row=2,column=3,padx=(15,0),pady=(5,5),sticky=E)
        
        #GUI - Input Boxes
        self.txt_browse1 = tk.Entry(self.master, width=50)
        self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(15,0),pady=(35,5),sticky=N+E+W)
        self.txt_browse2 = tk.Entry(self.master, width=50, text='')
        self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(15,0),pady=(5,5),sticky=N+E+W)
        
        
        #Need dialog modal that allows user to select folder directory, and have it show in the text field

#Funct. to insert filepath into Entry box
fileName1 = ''
fileName2 = ''
def browse_source(self):
    global fileName1
    fileName1 = fd.askdirectory()
    print(fileName1)
    self.txt_browse1.insert(END, fileName1)
    
def browse_dest(self):
    global fileName2
    fileName2 = fd.askdirectory()
    print(fileName2)
    self.txt_browse2.insert(END, fileName2)

### Build Function to run script    
def transfer():
    epoch24 = time.time() - 86400
    #def var for source path
    source = fileName1+'/'
    #def var for destination path
    destination = fileName2+'/'
    #Short script.. filters files ending in .txt then verifies modified time.
    #Moves .txt files that have been modified within 24hrs
    for file in os.listdir(source):
        if file.endswith(".txt"):
            file_time = os.path.getmtime(source+file)
            if file_time >= epoch24 and file.endswith(".txt"):
                shutil.move(source+file, destination)
          
#Funct. to close window
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
    


if __name__ == "__main__":
    root = tk.Tk()
    App = mainWindow(root)
    root.mainloop()