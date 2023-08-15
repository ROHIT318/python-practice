import os 

# Create a directory
os.mkdir("data")
print(os.listdir())

# Rename a file 
os.rename("data", "DATA")

# Get the folders present 
print(os.listdir())

# Get current file path
print(os.getcwd())

# Change directory
os.chdir("DATA/")
print(os.getcwd())

print(os.path.exists("data"))

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

# To read and write in a file
with open('/home/lol.txt', 'w') as content:
    content.write("This is file whose name is lol.txt; LOL")
with open('/home/lol.txt', 'r') as content:
    print(content.read())