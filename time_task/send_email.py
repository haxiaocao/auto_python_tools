#coding: utf-8
import smtplib
import base64

#reference site:
#https://www.tutorialspoint.com/python/python_sending_email.htm
#https://automatetheboringstuff.com/chapter16/
# note : you should format the Header carefully, most of errors come from it.


# For your programs, the differences between TLS and SSL aren’t important.
# You only need to know which encryption standard your SMTP server uses so you know how to connect to it.
# TLS->587, SSL->465
# smtpObj=smtplib.SMTP('smtp.163.com',25)
# smptpObj.ehlo()   #Get the smtpObj and then immediately say hello the smtp email server: 250 is success.
# smtpObj.starttls()
# smtpObj.login('myprojectok@163.com','xishuichangliu')
# smtpObj.sendmail('myprojectok@163.com','778104363@qq.com','content')
# smtpObj.quit()



sender = 'myprojectok@163.com'
receiver = '***@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'myprojectok@163.com'
password = ''

# smtpserver = smtplib.SMTP(smtpserver)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(username, password)
# header = 'To:' + receiver + '\n' + 'From: ' + sender + '\n' + 'Subject:testing \n'
# print header
# msg = header + '\n ShangHai weather is hot today ,20170819\n\n'
# smtpserver.sendmail(sender, receiver, msg)
# print 'done!'
# smtpserver.close()

###add the attachement file.

filename = "hello.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: myprojectok@163.com
To: guokai2007@163.com
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
msg = part1 + part2 + part3

try:
    smtpserver = smtplib.SMTP(smtpserver)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    smtpserver.sendmail(sender, receiver, msg)
    print 'done!'
    smtpserver.close()
except Exception as execp:
    print "Error: unable to send email"
    print str(execp)
