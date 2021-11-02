import smtplib
import os
from email.message import EmailMessage


if __name__ == "__main__":
        print("Sending Email")


        EMIAL_ADDRESS = "FoodWebsiteGenerator@gmail.com"
        EMIAL_PASSWORD = "cop452100"

        msg = EmailMessage()
        msg['From'] = EMIAL_ADDRESS
        msg['Subject'] = "Your Recipe"
        msg['To'] = "FoodWebsiteGenerator@gmail.com"
        msg.set_content("This is a test")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(EMIAL_ADDRESS,EMIAL_PASSWORD)
            smtp.send_message(msg)