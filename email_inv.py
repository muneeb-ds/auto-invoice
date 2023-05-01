from datetime import datetime
import smtplib
from decouple import config
import os

from email.message import EmailMessage

EMAIL_ADDRESS = config('EMAIL')
PASSWORD = config('PASS')

class EmailUpdate:

    def __init__(self, receiver):
        self.receiver = receiver

    def mail_msg(self):
        date = datetime.today()
        month = date.strftime('%b')
        year = date.year

        msg = EmailMessage()
        msg['Subject'] = f"Invoice {month}-{year}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.receiver

        msg.set_content(f"PSA for {month}'s invoice\n\nRegards.")
        with open(f'invoices/invoice_{month}_{year}.xlsx', "rb") as f:
            attachment = f.read()

        msg.add_attachment(attachment, maintype="application", subtype='xlsx', filename=f"invoice_{month}_{year}.xlsx")
        
        return msg

    def connect(self, smtp):
        smtp.login(EMAIL_ADDRESS, PASSWORD)

    def send(self):
        msg = self.mail_msg()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        # with smtplib.SMTP("localhost", 1025) as smtp:
            self.connect(smtp)
            smtp.send_message(msg)