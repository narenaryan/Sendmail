import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#sendmail(target,username,password,subject,body,html(or)plain)
def sendmail(to_addr,username,password,subject,body,html=False):
    #connect to server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #create header part of mail
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_addr
    msg['Subject'] = subject
    if html:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    #Next, log in to the server
    server.starttls()
    server.login(username,password)
    #Send the mail
    mail = msg.as_string() # The /n separates the message from the headers
    print server.sendmail("you@gmail.com", "narenarya@live.com", mail)
