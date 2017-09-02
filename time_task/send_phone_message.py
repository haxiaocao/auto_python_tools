# accountSID = 'AC1f90bb7fe2c9430fe197a91461df8cd8'
# authToken = '4e9ca120f56ba605653620559b0ce969'
# myNumber = '+86**'
# twilioNumber = '+1555***8'
#
# # The to, from_, and body attributes should hold your cell phone number, Twilio number, and message, respectively.
# # Note that the sending phone number is in the from_ attribute—with an underscore at the end—not from.  This is because from is a keyword in Python
# # (you’ve seen it used in the from modulename import * form of import statement, for example), so it cannot be used as an attribute name.
# from twilio.rest import TwilioRestClient
#
# def send_text_myself(message):
# 	twilioCli = TwilioRestClient(accountSID, authToken)
# 	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
#
# send_text_myself('good afternoon, and send you a message for hello')


#reference site： https://github.com/ksdme/py-textbelt
from pytextbelt import Textbelt

Recipient = Textbelt.Recipient("1122334455", "us")
reponse = Recipient.send("Hello World!")
reponse = Recipient.send("Its me, The Bot.")
