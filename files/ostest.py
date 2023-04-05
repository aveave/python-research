import os

#  current working directory
print(os.getcwd())

# Creates a new directory with the specified path
# os.mkdir('anotherfolder')
# os.mkdir('/Users/eaverkin/Projects/python/python-research/files/absolutepath')

# Returns a list of files and directories in the specified directory. The default is the current working directory.
# print(os.listdir(path='.'))
print(os.listdir(path='/Users/eaverkin/Projects/python/python-research/files'))

# removes file, folder can't be removed
# os.remove('anotherfolder/test.txt')

# Checks
# Returns True if the file or directory at the specified path exists, and False otherwise.
file = 'anotherfolder/test.txt'
if os.path.exists(file) and os.path.isfile(file):
    os.remove(file)
file = 'anotherfolder/test'
if os.path.exists(file) and os.path.isdir(file):
    os.rmdir(file)


# Removes the directory at the specified path. The directory must be empty.
# os.rmdir('/Users/eaverkin/Projects/python/python-research/files/absolutepath')

# Recursive directory creation function, like mkdir(), 
# but creates all intermediate-level directories needed to contain the leaf directory.
# os.makedirs('anotherfolder/subfolder/sub')

# Removes the directory and any intermediate-level directories required to remove the leaf directory. 
# If any of the intermediate-level directories are non-empty, an error is raised.
# os.removedirs('anotherfolder/subfolder/sub')