import os
cmd = input('Which cmd do you want run?')
fp = os.popen(cmd)
res = fp.read()
fp.close()
print (res)
