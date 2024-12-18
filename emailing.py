import smtplib
from email.message import EmailMessage
import email
import imghdr
import os
import ssl

PASSWORD = os.getenv("PASSWORD")


def send_email(image_path):
    email_message = EmailMessage
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("vattyam.sandeep@gmail.com", password=PASSWORD)
    gmail.sendmail("vattyam.sandeep@gmail.com",
                   "vattyam.sandeep@gmail.com",
                   email_message.as_string())
    gmail.quit()

if __name__ == "__main__" :
    send_email(image_path="images/19.png")





