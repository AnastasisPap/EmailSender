EMAIL_ADRESS = "your_email"
PASSWORD = "your_password"
TARGET_EMAIL = input('Who do you want to send email to? ')
if(TARGET_EMAIL.find('@') == -1):
    print('Please enter a valid email')
    TARGET_EMAIL = input('Who do you want to send this email to? ')

SUBJECT = "Raspberry pi image"
MESSAGE = "This is an image sent from a raspberry pi!"
