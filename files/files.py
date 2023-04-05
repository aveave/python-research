# When we want to read from or write to a file, we need to open it first. 
# When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:

# Open a file
# Read or write (perform operation)
# Close the file

file = open('test.txt')
file1 = open('test.txt', 'r')

print(file.read())
file.close()

# When we are done with performing operations on the file, we need to properly close the file.

# Closing a file will free up the resources that were tied with the file. It is done using the close() method in Python.

# we can close with try finally or

with open('test.txt', 'r') as newfile:
    print('read everything')
    print(newfile.read())

with open('test.txt', 'r') as newfile:
    print('read one line')
    print(newfile.readline())
# readlines()
# So, the primary difference between read() and readlines() is that 
# read() reads the entire file as a single string, 
# whereas readlines() reads the file line by line and returns a list of strings.

# with...open - better


# Write to a file
#If we try to open a file that doesn't exist, a new file is created.
#If a file already exists, its content is erased, and new content is added to the file.

with open('test.txt', 'r') as read:
    characters = 0
    for line in read:
        characters += len(line)
# write
# with open('newtest.txt', 'w') as new:        
#     new.write(f"Amount of characters is {characters}")
# append
with open('newtest.txt', 'a') as new:        
    new.write(f"Amount of characters is {characters} \n")