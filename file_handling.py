
# Opening modes r for read, a for append, w for write
f = open('README.md', 'r')
print(f.name)       # 'README.md'
print(f.mode)       # 'r'

# Close the file each time you open it
f.close()

with open('test.txt', 'w') as fw:
    fw.write("This is a sentence.\nThis is a new sentence.")


## Open file using context manager so that it gets closed automatically
with open('README.md', 'r') as f:
    print(f.name)       # 'README.md'
    file_content_read = f.read()
    print(file_content_read)         # Displays all the contents of the file in proper format

    # Takes the pointer to the beginning of the file
    f.seek(0)

    # Returns all the content of the file with '\n' being at the end of the line.
    file_content_readlines = f.readlines()
    print(file_content_readlines)

    f.seek(0)

    file_content_readline = f.readline()        # File Definition
    print (file_content_readline)


    # Read the file line by line
    for line in f:
        print(line, end=' ')        # Displays entire file content  

    f.read(100)                     # Reads first 100 characters of a file

print(f.closed)         # True