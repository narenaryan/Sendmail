Sendmail
========

Sends mail as plain text or html and wraps the basic SMTP library in python

The Usage is in this way.

from Sendmail import sendmail

sendmail(to_address,
         username,
         password,
         subject,
         body,
         html=True) #if body is HTML content else False
         
