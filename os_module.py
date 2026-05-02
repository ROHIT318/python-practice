import os 

# Create a directory
os.mkdir("data")
print(os.listdir())

# Rename a file (old_file_name, new_file_name)
os.rename("data", "DATA")

# Get the folders present 
print(os.listdir())

# Get current file path
print(os.getcwd())

# Change directory
os.chdir("DATA/")
print(os.getcwd())

# To check whether the filepath exists. True if exists else False.
print(os.path.exists("/data/"))

# Get OS information name
print(os.name)
print(os.uname())

# Get file directories information
for files in os.scandir('/home/'):
    if files.is_dir() == True:
        print("{} is a directory".format(files.name))
    else:
        print("{} is a file".format(files.name))

# To create a file 
os.mkdir("lol.txt")
print(os.listdir())

# Delete a directory
os.rmdir('/delete/')

# Delete intermediate directories
os.removedirs('/delete/delete_folder')

# all_files_path = []
# for root, dirs, files in os.walk('<file-path>'):
#       all_files_path.append(os.path.join(root, files))

# # Get directory name from the path
# print(os.path.dirname('<file-path>'))     # directory-file-path

# # Get file name from the path
# print(os.path.basename('<file-path>'))    # filename

# # In case you want to get both directory and file name
# print(os.path.split('<file-path>'))       # ('<dir-name>', 'filename')

# # In case we want to split both filepath and extension of the file.
# print(os.path.splitext('<file-path>'))    # ('<dir-name>/filename', '.ext')

# To read and write in a file
with open('/home/lol.txt', 'w') as content:
    content.write("This is file whose name is lol.txt; LOL")
with open('/home/lol.txt', 'r') as content:
    print(content.read())