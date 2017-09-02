import imapclient
import imaplib
import pyzmail

# ISSUE: 163没有能够使用成功！！！
#reference site: https://automatetheboringstuff.com/chapter16/
#imap: internet message access protocol -> retrieve emails
#The imapclient module downloads emails from an IMAP server in a rather complicated format. Most likely,
# you wil want to convert them from this format into simple string values. The pyzmail module does
# the hard job of parsing these email messages for you.

# imapObj=imapclient.IMAPClient('imap.163.com')
imapObj=imaplib.IMAP4('imap.163.com',993)

print 'ok'
# imapObj.login('','')
# imapObj.select_folder('',readonly=True)
# UIDs=imapObj.search(['SINCE 05-Jul-2014'])
# print UIDs
#
# rawMessage=imapObj.fetch([40041],['BODY[]','FLAGS'])
# message=pyzmail.PyzMessage.factory(rawMessage[40041]['BODY[]'])
#
# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('cc')
# message.get_addresses('bcc')
#
# message.text_part!=None
# message.text_part.get_payload().decode(message.text_part.charset)
# message.html_part!=None
# message.html_part.get_payload().decode(message.html_part.charset)
# imapObj.logout()
