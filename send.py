from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")

class SendMessage:
    def __init__(self,name,email,message):
        self.sender_email=email
        self.sender_name=name
        self.sender_message=message
    
    def from_sender(self):
        with SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email,to_addrs=email,msg=f"Subject: Message from Portfolio \n\nName:{self.sender_name}\n"+\
                                f"Email: {self.sender_email}\n"+\
                                    f"Message: {self.sender_message}")
    def to_sender(self):
        with SMTP("smtp.gmail.com",port=587) as connection_second:
            connection_second.starttls()
            connection_second.login(user=email,password=password)
            connection_second.sendmail(from_addr=email,to_addrs=self.sender_email,msg=f"Subject:Birochan Received the message\n\n"+\
                                       f"Thank you! Your message has been received and I will get back to you shortly.\n"+\
                                        f"Regards,\nBirochan")