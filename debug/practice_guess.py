import random
import logging

def judge_guess(guess,toss):
    if ((guess =="heads" and toss==0) or (guess =="tails" and toss==1)):
        return True
    else:
        return False

logging.basicConfig(filename="debug_guess.txt",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input()

logging.debug('your first guess is :'+ guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Random number is :'+ str(toss))
result=judge_guess(guess,toss)
if(result):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = raw_input()
    logging.debug("Your Second guess:"+ guess)
    assert guess in ('heads','tails'), "Your input guess must be in ('tails','heads') "
    result=judge_guess(guess,toss)
    if(result):
        print 'you got it!'
    else:
        print 'Nope. You are really bad at this game.Have No another chance .'

logging.info("The program get the last real log in the records.")
logging.disable(logging.CRITICAL)
logging.info("The program is going to be end.")
logging.info("Good bye......")
