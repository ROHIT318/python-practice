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