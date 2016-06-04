#Directory operations
import os

#Prints out all the attributes and methods available in the module
print(dir(os))

#Finds current directory
currentDirectory = os.getcwd()
print(currentDirectory)

#Change current directory
#pass in the path as a string
os.chdir('/Users/Nathan Jiang/Desktop/')

#Shows the files available at a certain directory
#By default, it chooses the current directory
#Returns as a list of strings
print(os.listdir())

#Makes a new folder in your current directory
#os.mkdir('newDirectory2/subDirectory') will give error cause newDirectory2 doesnt exist
os.mkdir('newDirectory')

#Makes a new directory. Can be a couple levels deep.
#This will make both newDirectory (which doesn't exist yet) and subDirectory
#This option is preferable over mkdir
os.makedirs('newDirectory2/subDirectory')

#Renames a selected directory
#Original, New name
os.rename('newDirectory','newDirectory3')

#Deletes directory specified. Will not delete intermediate directories
#Therefore, only subDirectory will be removed
#this is preferable
os.rmdir('newDirectory2/subDirectory')

#Deletes specified and intermediate directory
#In this case, both newDirectory2 and Subdirectory will be removed
#####os.removedirs('newDirectory2/subDirectory')

#Returns information about the selected file
#includes size, last modification time, 
os.stat('demo.txt')

#Traverses an entire directory tree from top down.
#Traverses the directory tree depth first
#Generator that yields a tuple of 3 values as it walks the directory tree
#For each directory, it yields the directory path, directories within that path, and files within that path
for dirpath, dirname, filenames in os.walk(os.getcwd()):
    print(dirpath, dirname, filenames)

#Gets the environment variables
#The example below gives the home directory
os.environ.get('HOME')

#combines a path and a file name
file_name = 'file.txt'
file_path = os.path.join(os.environ.get('HOME'), file_name)

#Gives us the base name of the path we specified (i.e the file name)
os.path.basename('/asd/test.txt') #gives us text.txt

#Gives us the directory name of the path we specified 
os.path.basename('/asd/test.txt') #gives us /asd

#Splits the pathname into parts
os.path.split('/asd/test.txt') #gives us ('/asd', 'test.txt')
#Splits the file root and the extension
#Easier than string splicing
os.path.splittext('/asd/test.txt') #gives us ('/asd/test','.txt')

#Checks if a path exists
os.path.exists(path)

#checks if something is a directory or a file
os.path.isdir('/asd/test')
os.path.isfile('/asd/test')
