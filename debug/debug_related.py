#reference: https://automatetheboringstuff.com/chapter10/

# Exception
#traceback
#assert    --Assertions can be disabled by passing the -O option when running Python.
#logging    --[don't use print for debugging] you can always disable them later by adding a single logging.disable(logging.CRITICAL) call.
#           --logger level: debug -> info -> warning -> error-> critical
#debuggers  --in IDLE editor

# Assertions are for programmer errors, not user errors. For errors that can be
# recovered from (such as a file not being found or the user entering invalid data),
# raise an exception instead of detecting it with an assert statement.



# import traceback

# try:
#     raise Exception('This is the error message')
# except:
#     errorFile=open('errorInfo.txt','w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print " The traceback info was written to the errorInfo.txt."


# podBayDoorStatus='open'
# assert podBayDoorStatus=='open','The pod bay doors need to be "open"'
# podBayDoorStatus='can not open this door'
# assert podBayDoorStatus=='open', 'The pod bay doors need to be "open"'
