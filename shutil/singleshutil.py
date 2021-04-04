import shutil
import os

source = '/Users/Deepak/Desktop/folderA/'

destination = '/Users/Deepak/Desktop/folderB/'
files = os.listdir(source)

for file in files:
    shutil.move(source+i, destination)
