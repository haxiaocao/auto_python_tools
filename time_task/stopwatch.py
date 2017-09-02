#reference site;https://automatetheboringstuff.com/chapter15/
# stopwatch.py - A simple stopwatch program.

import time

print '''Print the enter key to begin the stopwatch , and then print the enter key to stop it.
        And press the CTRL-C to quit.'''

a=raw_input()
print 'Get started.........'
start=time.time()
lasttime=start
lapNum=1

#start tracking the lap time
try:
    while True:
        b=raw_input()
        lapTime=round(time.time()-lasttime,2)
        totalTime=round(time.time()-start,2)
        print 'Lap #%s:%s (%s)' % (lapNum,totalTime,lapTime)
        lapNum+=1
        lasttime=time.time() #reset the last lap time
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying.
    print 'All done....'
