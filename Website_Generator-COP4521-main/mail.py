import smtplib
import os
from email.message import EmailMessage

class mail:
    def __init__(self,sendTo,subject,msg):
        self.sendTo = sendTo
        self.subject = subject
        self.message = msg

    def sendMessage(self):
        EMIAL_ADDRESS = "FoodWebsiteGenerator@gmail.com"
        EMIAL_PASSWORD = "cop452100"

        msg = EmailMessage()
        msg['From'] = EMIAL_ADDRESS
        msg['Subject'] = self.subject
        msg['To'] = self.sendTo
        msg.set_content(msg)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(EMIAL_ADDRESS,EMIAL_PASSWORD)
            smtp.send_message(msg)


if __name__ == "__main__":
        print("Sending Email")
        email = "FoodWebsiteGenerator@gmail.com"
        subject = "Your Recipe"
        msg = "This is a test"

        userMail = mail(email,subject,msg)
        userMail.sendMessage()
