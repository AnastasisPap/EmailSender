import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import config

#Email used to send the image
email_user = config.EMAIL_ADRESS
#Target email
email_send = config.TARGET_EMAIL
#Subject of the email
subject = config.SUBJECT

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = config.MESSAGE
msg.attach(MIMEText(body, 'plain'))

#Filename with the path
filename = '/home/pi/Pictures/image.jpg'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= ' + filename)

msg.attach(part)
text = msg.as_string()

#Email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, config.PASSWORD)

server.sendmail(email_user, email_send, text)
server.quit()
