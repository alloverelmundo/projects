import os;

folder = '/Users/vk/Desktop/vscodepractice/'

#checking the files and directories in a folder

entries = os.scandir(folder);

for entry in entries:
    if os.path.isfile(entry):
        print('file: '+ entry.name)
    elif os.path.isdir(entry):
        print('directory: '+ entry.name)

#moving a file
        
originalfolder = '/Users/vk/Desktop/vscodepractice/'
destinationfolder = '/Users/vk/Desktop/CleanedUp/'

os.mkdir(destinationfolder)

for entry in os.scandir(originalfolder): #list the entries in the desktop folder

    originallocation = os.path.join(originalfolder, entry.name) #in order to move the files, we need to create the paths first      
    destinationlocation = os.path.join(destinationfolder, entry.name)

    if os.path.isfile(entry):
        os.rename(originallocation, destinationlocation); #rename allows us to move a file to a new path

#chat gpt code

import os

originalfolder = '/Users/vk/Desktop/vscodepractice/'
destinationfolder = '/Users/vk/Desktop/CleanedUp/'

# Check if the destination folder exists, if not, create it
if not os.path.exists(destinationfolder):
    os.mkdir(destinationfolder)

for entry in os.scandir(originalfolder):
    originallocation = os.path.join(originalfolder, entry.name)
    destinationlocation = os.path.join(destinationfolder, entry.name)

    if entry.is_file():  # Check if it's a file
        os.rename(originallocation, destinationlocation)

