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







    



import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email import Encoders

# Limpiando la pantalla con el comando "cls" de windows (si te encuentras en un SO basado en unix cambiarlo a "clear")


def check(mail):
  delimiter = '@' in mail
  if delimiter == False:
	  
	  exit()

def email_option_body(msg):
	option = 0
	while True:
		
		try:
			option = int(raw_input("Elige una opcion: "))
		except ValueError:
			raw_input("\nLo siento, no entendi eso :c\n")
			continue
		else:	
			if option != 1 and option != 2:
				continue
			if option == 1:
				file_path = raw_input("Ruta de archivo con extension: ")
				if ".txt" in file_path:
					file = open(file_path, 'r')
					msg.attach(MIMEText(file.read()))
					file.close()
					break
				elif ".html" in file_path:
					file = open(file_path, 'r')
					msg.attach(MIMEText(file.read(), 'html'))
					file.close()
					break
				else:
					raw_input("Archivo invalido! Extensiones validas *.txt, *.html")
					continue
			else:
				data = raw_input("Escribe el mensaje\n ")
				msg.attach(MIMEText(data))
				break


raw_input("Presiona ENTER para continuar :^)")


mail_f = raw_input()
check(mail_f)
mail_t = raw_input()
check(mail_t)

print
sub = raw_input()

msg = MIMEMultipart()
msg['From'] = mail_f
to = []
msg['To'] = to.append(mail_t)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = sub

email_option_body(msg)

# Agrega aqui el ID y PASSWORD de SMPT2GO
# --> www.SMTP2GO.com
ID = "id" #Tu user ID
PASS = "clave" #Tu Clave

# Enviar email
try:
	server = smtplib.SMTP("smtpcorp.com", 2525)
	server.ehlo()
	server.starttls()
	server.login(ID,PASS)
	server.sendmail(mail_f, mail_t, msg.as_string())
	server.close()
	
except smtplib.SMTPException:
	pass