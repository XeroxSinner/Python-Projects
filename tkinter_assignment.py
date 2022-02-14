

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

class mainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("Check Files")
        
        
        #GUI - Buttons
        self.btn_browse = tk.Button(self.master,width=15, height=1, text="Browse..", command=lambda: browse(self))
        self.btn_browse.grid(row=0,column=0,padx=(15,0),pady=(35,5),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15, height=1, text="Browse..")
        self.btn_browse2.grid(row=1,column=0,padx=(15,0),pady=(5,5),sticky=W)
        self.btn_check = tk.Button(self.master,width=15, height=2, text="Check for Files..")
        self.btn_check.grid(row=2,column=0,padx=(15,0),pady=(5,5),sticky=W)
        self.btn_close = tk.Button(self.master,width=15, height=2, text="Close Program")
        self.btn_close.grid(row=2,column=3,padx=(15,0),pady=(5,5),sticky=E)
        
        #GUI - Input Boxes
        self.txt_browse1 = tk.Entry(self.master, width=50)
        self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(15,0),pady=(35,5),sticky=N+E+W)
        self.txt_browse2 = tk.Entry(self.master, width=50, text='')
        self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(15,0),pady=(5,5),sticky=N+E+W)
        
        
        #Need dialog modal that allows user to select folder directory, and have it show in the text field

def browse(self):
    fileName = fd.askopenfilename()
    print(fileName)
    self.txt_browse1.insert(END, fileName)


        
        
        
        





## Added mainloop() for work in VSCode to keep window open
if __name__ == "__main__":
    root = tk.Tk()
    App = mainWindow(root)
    root.mainloop()
    
    
    