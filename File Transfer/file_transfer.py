import shutil
import os

#sets source files
source = 'C:/Users/nylan/Desktop/FolderA/'

#sets destination
destination = 'C:/Users/nylan/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)

