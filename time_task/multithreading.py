###https://automatetheboringstuff.com/chapter15/
import threading,time

# print 'Start this program....'
#
# def take_a_Nap():
#     time.sleep(5)
#     print 'wake up this morning.'
#
# threadObj=threading.Thread(target=take_a_Nap)
# threadObj.start()
#
# print 'End of the program....'

# print 'Start this program.....'
# def take_a_nap_with_args(seconds,greetings):
#     print greetings
#     time.sleep(seconds)
#
# thread_args=threading.Thread(target=take_a_nap_with_args,args=(3,'Good morning'))
# thread_args.start()
#
# print 'This program will the end....'


### open new process
#subprocess.Popen()

def print_numbers(a,b):
    for i in range(a,b):
        print i

threads=[]
for i in range(0,50,10):
    t=threading.Thread(target=print_numbers,args=(i,i+9))
    threads.append(t)
    t.start()

for tt in threads:
    tt.join()

print "ALL THREAD IS DONE."
