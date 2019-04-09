import os
from os.path import join
searchDir = input('In which dir do you want search the Files? ')
fileExt = input('What is the extension of that file?')
for (dirname, dirs, files) in os.walk(searchDir):
   for filename in files:
       if filename.endswith(fileExt):
           thefile = os.path.join(dirname,filename)
           print (os.path.getsize(thefile), "  -  " , thefile)
