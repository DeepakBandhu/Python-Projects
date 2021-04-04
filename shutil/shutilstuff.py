import shutil
import os

source = '/Users/Deepak/Desktop/folderA/'

destination = '/Users/Deepak/Desktop/folderB/'
files = os.listdir(source)

for file in files:
	new_path = shutil.move(f"{source}/{file}", destination)
	print(new_path)
