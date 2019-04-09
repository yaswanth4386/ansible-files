# how many  files had in the sub-folders
import os
searchDir = input('In which dir do you want search the Files? ')
fileExt = input('What is the extension of that file?')
totCount = 0
for (dirname, dirs, files) in os.walk(searchDir):
   count = 0;
   print ("List of all the Dirs : ", dirs)
   print ("List of all the Files : ", files)
   print ("Directory Name : ", dirname)
   for filename in files:
       #print "The file Name : %s " % filename
       if filename.endswith(fileExt) :
           count = count + 1
           totCount+=1
   print ('Total Files in ', dirname, ' is : ', count)
print ('Total Number of Files are : ', totCount)
