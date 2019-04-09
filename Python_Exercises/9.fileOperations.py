import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive
fileName = "test.txt"
newFileName = "test.txt.bak"
def main():

# get the path to the file in the current directory
		src = path.realpath(fileName);
# Process 1 : now put things into a ZIP archive
		root_dir,tail = path.split(src)
		print (root_dir , "   " , tail)
		shutil.make_archive("fileSize_archive", "zip", root_dir)
		
# Process 2 : more fine-grained control over ZIP files
		with ZipFile("testFileSize.zip","w") as newzip:
			for (dirname, dirs, files) in os.walk("."):
				for filename in files:
					if filename.endswith(".py"):
						newzip.write(filename)			
	#else:
	   # print fileName, " is not available"
if __name__== "__main__":
	  main()
