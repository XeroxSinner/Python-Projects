from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

class Window(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title("Form Title")
        self.pack(fill = 'both', expand = 1)

        self.filepath = tk.StringVar()

        quitButton = tk.Button(self, text = 'Quit',
                               command = self.close_window)
        quitButton.place(x = 0, y = 0)

        browseButton = tk.Button(self, text = 'Browse',
                                 command = self.first_browser)
        browseButton.place(x = 0, y = 30)

        filepathText = tk.Entry(self, textvariable = self.filepath)
        filepathText.pack()

    def close_window(self):
        form.destroy()

    def show_file_browser(self):
        self.filename = filedialog.askopenfilename()
        return self.filename

    def first_browser(self):
        file = self.show_file_browser()
        self.filepath.set(file)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = Window(root)
    root.mainloop()