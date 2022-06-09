from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
class EmailSpoof:
    def __init__(self):
        pass

    def spoof(self,toemail,toname,sendername,senderemail,message,subject,realemail,realemailpassword):
        # Real email credentials
        username = realemail
        password = realemailpassword

        # Fake Credentials
        fake_from = senderemail
        fake_name = sendername

        # Target credentials
        to_email = toemail
        to_name = toname

        # Message to be sent
        content = message

        message1 = MIMEMultipart('alternative')
        message1.set_charset("utf-8")
        print(senderemail)
        message1["From"] = sendername+ "<" +  "jayantkhanna31052002@gmail.com" + ">"
        message1['Subject'] = subject
        message1["To"] = toemail
        body = MIMEText(content, 'html')
        message1.attach(body)
        # Creating server instance 
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # Starting TLS
        server.starttls()
        # Login into server using correct email
        server.login(username, password)
        # Sending Mail
        server.sendmail("ayantkhanna31052002@gmail.com", to_email, message1.as_string())
        # CLosing Server
        server.close()
        # App password
        #icdgjxokvhtsvfex


    def compose_message(self, sender, name, recipients, subject, html):
        self.sender = sender
        self.recipients = recipients

        message = MIMEMultipart('alternative')
        message.set_charset("utf-8")

        message["From"] = name + "<" +  self.sender + ">"
        message['Subject'] = subject
        message["To"] = ', '.join(self.recipients)

        body = MIMEText(html, 'html')
        message.attach(body)
        return message;







    