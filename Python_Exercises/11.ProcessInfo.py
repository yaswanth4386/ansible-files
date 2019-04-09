import os, string
 
program = input("Enter the name of the program to check: ")
 
#try:
    #perform a ps command and assign results to a list
fp = os.popen("ps -f|grep " + program)
output = fp.read()
print (output)

proginfo = string.split(output)
 
    #display results
print ("\n\
    Full path:\t\t", proginfo[5], "\n\
    Owner:\t\t\t", proginfo[0], "\n\
    Process ID:\t\t", proginfo[1], "\n\
    Parent process ID:\t", proginfo[2], "\n\
    Time started:\t\t", proginfo[4])
#except:
    #print ("There was a problem with the program.")
