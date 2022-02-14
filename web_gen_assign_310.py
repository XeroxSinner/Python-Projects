"""
Create script that creates and opens a new html file
"""

import webbrowser
import web_gen_assign


def browserOpen(self):
    webbrowser.open_new_tab('demohtml.html')


# def submit(self):
#     inputVar = web_gen_assign.self.txt_input.get()
#     f = open("demohtml.html", "w")
#     f.write("<html> \n <body> \n <h1>" + inputVar +"</h1> \n </body> \n </html> ")
#     f.close()
#     f = open("demohtml.html", "r")
#     print(f.read())



