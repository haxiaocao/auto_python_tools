#Time module:  time, datetime
#task: subprocess , threading.

import time

# def calcProd():
#     ''' Calculate the prodoct of the first 100000 numbers.'''
#     product=1
#     for i in range(1,100000):
#         product=product*i
#     return product
#
# startTime=time.time()
# prod=calcProd()
# endTime=time.time()
# print "Result is {} digit long.".format(len(str(prod)))
# print "It took {} seconds to calculate the result.".format(endTime-startTime)

# ###Note the time.spleep(1)  is waiting for 1 seconds here.
# for i in range(3):
#     print 'good morning'
#     time.sleep(10)
#     print "Hello world."
#     time.sleep(100)
#
# time.sleep(5)
# print 'It is the end of the program.'

# datetime to string format: t.strftime('%Y %m %d %H:%M:%S')
import datetime
print datetime.datetime.now()
dt=datetime.datetime(2015,10,21,16,29,0)
