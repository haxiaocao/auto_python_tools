import time
import subprocess

timeleft=10
while timeleft>0:
    print 'timeleft, end='+str(timeleft)
    time.sleep(1)
    timeleft=timeleft-1

print 'Clock is down....'
# On Windows, be sure to include 'start' in the list you pass to Popen() and pass the keyword argument shell=True.
subprocess.Popen(['start','alarm.wav'],shell=True)

# 'start'  is for windows[equivalent of double clicking], and will the default application to open the files.
subprocess.Popen([r"start",'hello.txt'],shell=True)
