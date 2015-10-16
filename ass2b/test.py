#!/usr/bin/python
import subprocess
import smtplib

sender = 'bitter.auto@bitter.com'
receivers = ['markshen5295@hotmail.com']

message = """From: From Person <bitter.auto@bitter.com>
To: To Person <markshen5295@hotmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
