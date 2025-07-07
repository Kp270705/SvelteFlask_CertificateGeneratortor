import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PythonTasks.passwordsInfo import password3

def send_mails(email_sender, email_receiver, file_path, eventname, cert_type):
    print("\n\nIn send_mails")

    email_subject = f"Your {eventname} certificate."
    email_body = f"This is to inform you, we just sent your {eventname}'s certificate {cert_type}."
    password = password3

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'plain'))

    # open the file to send:
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())

    encoders.encode_base64(p)
    p.add_header("Content-Disposition", f"attachment; filename={filename}")

    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, f"{password}")

    text = msg.as_string()
    server.send_message(msg)
    server.quit()

    print("\tMessage sent successfully....\n")
    print(f"------------------------------------------------------\n")