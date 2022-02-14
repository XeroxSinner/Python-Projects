"""
- Create GUI allowing for input text
- Utilize input text to edit existing HTML file
- Two(?) Buttons?
    - Submit Text
        - Some sort of if file doens't exist.. though 'w' seems to work fine
    - Open webpage
"""
#Importing necessary modules
from tkinter import *
import tkinter as tk
import webbrowser

#Building the tkinter GUI
class mainWindow(Frame):
    def __init__(self,master,*args, **kwargs ):
        Frame.__init__(self, master,*args, **kwargs)
        
        self.master = master
        self.master.minsize(600,600)
        self.master.maxsize(600,600)
        center_window(self,600,600)
        self.master.title("Web Site Generator")
    
        #Label with instructions goes here
        self.lbl_self = tk.Label(self.master,text="How to make simple page.")
        self.lbl_self.grid(row=0,column=0,columnspan=2,padx=(10,10),pady=(5,5), sticky=N)
        self.lbl_self1 = tk.Label(self.master,text="Step 1: Type what you'd like displayed and hit submit.")
        self.lbl_self1.grid(row=1,column=0,columnspan=2,padx=(10,10),pady=(5,5), sticky=N)  
        self.lbl_self2 = tk.Label(self.master,text="Step 2: Click that Open button. Ezpz!")
        self.lbl_self2.grid(row=2,column=0,columnspan=2,padx=(10,10),pady=(5,5), sticky=N)          
        
        #Entry box
        self.txt_input = tk.Entry(self.master, width=95)
        self.txt_input.grid(row=3,column=0,columnspan=2,padx=(10,0), pady=(0,5), sticky=N)
        
        #Button to submit entry goes here
        self.btn_submit1 = tk.Button(self.master,width=20,height=1, text="Submit", command=lambda: submit(self))
        self.btn_submit1.grid(row=4, column=0, padx=(10,0),sticky=W)
        self.btn_submit2 = tk.Button(self.master,width=20,height=1, text="Open Browser", command=lambda: browserOpen(self))
        self.btn_submit2.grid(row=4, column=1, sticky=E)


#Functions
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def submit(self):
    inputVar = self.txt_input.get()
    f = open("demohtml.html", "w")
    f.write("<html> \n <body> \n <h1>" + inputVar +"</h1> \n </body> \n </html> ")
    f.close()
    f = open("demohtml.html", "r")
    
def browserOpen(self):
    webbrowser.open_new_tab('demohtml.html')
    

####
if __name__ == "__main__":
    root = Tk()
    App = mainWindow(root)
    root.mainloop()
        
    