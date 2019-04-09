import sys
print ('Count : ', len(sys.argv) - 1)
count = 0;
for arg in sys.argv:
   print ('Argument ', count, " : ", arg)
   count += 1
