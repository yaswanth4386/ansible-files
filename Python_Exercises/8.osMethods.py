## Check for File existence and is it a file or dir
import os
from os import path
import datetime
from datetime import date, time
import time
fileName = "6.fileSize.py"
def main():
    # Print the name of the OS
    print (os.name)
    if path.exists(fileName) == True:
        # Check for item existence and type
        print ("Item exists: " + str(path.exists(fileName)))
        print ("Item is a file: " + str(path.isfile(fileName)))
        print ("Item is a directory: " + str(path.isdir(fileName)))
        # Work with file paths
        print ("Item's path: " + str(path.realpath(fileName)))
        print ("Item's path and name: " + str(path.split(path.realpath(fileName))))
	#Get the modification time
        t = time.ctime(path.getmtime(fileName))
        print (t)
    else:
        print (fileName, " is not available")
main()
