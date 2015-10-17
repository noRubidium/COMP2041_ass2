#!/usr/bin/python
import subprocess
import smtplib

sender = 'bitter.auto@bitter.com'
receivers = ['markshen5295@gmail.com']

message = """From: From Person <bitter.auto@bitter.com>
To: To Person <markshen5295@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com')
smtpObj.login('comp2041ass2ms@gmail.com','12345qazwsx')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
# comp2041ass2ms@gmail.com
# 12345qazwsx