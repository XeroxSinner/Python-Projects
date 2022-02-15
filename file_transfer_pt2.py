"""
    - Pull all text files from one folder to another
        - Must only be text files modified or created in the past 24hrs
"""

import os
import shutil
import time


#Sets var with timestamp from 24hrs ago
epoch24 = time.time() - 86400


#def var for source path
source = 'C:/Users/nylan/Desktop/FolderA/'
#def var for destination path
destination = 'C:/Users/nylan/Desktop/FolderB/'


#Short script.. filters files ending in .txt then verifies modified time.
#Moves .txt files that have been modified within 24hrs
for file in os.listdir(source):
    if file.endswith(".txt"):
        file_time = os.path.getmtime(source+file)
        if file_time >= epoch24 and file.endswith(".txt"):
            shutil.move(source+file, destination)
        
