import os
import shutil

#create folders
os.mkdir('reference2')

#delete folders
if os.path.exists('reference2'):
    shutil.rmtree('reference2')

#delete files
os.remove(r"./")

#move files or folders
shutil.move("./","../")

#view the information of all files in the folder
for files in os.walk(r"./"):
    print(files)
    print(files[2])
