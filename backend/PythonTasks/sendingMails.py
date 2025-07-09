import smtplib, os
from concurrent.futures import ThreadPoolExecutor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PythonTasks.passwordsInfo import password3

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
MAX_WORKERS = 4          # 4 parallel connections
SENDER = "kunalpathak4774@gmail.com"

def build_msg(to_addr, file_path, event, ctype):
    msg = MIMEMultipart()
    msg["From"], msg["To"] = SENDER, to_addr
    msg["Subject"] = f"Your {event} certificate"
    msg.attach(MIMEText(
        f"Hi,\n\nAttached is your {event} {ctype}.\n\nBest.", "plain"))

    fn = os.path.basename(file_path)
    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={fn}")
    msg.attach(part)
    return msg

def send_one(args):
    to_addr, pdf, event, ctype = args
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20)
        server.starttls()
        server.login(SENDER, f"{password3}")
        server.send_message(build_msg(to_addr, pdf, event, ctype))
        server.quit()
        print(f"✅ {to_addr}")
    except Exception as e:
        print(f"❌ {to_addr}: {e}")

def send_bulk_parallel(recipients, event, ctype):
    # recipients = [(email, pdfPath), ...]
    with ThreadPoolExecutor(MAX_WORKERS) as ex:
        ex.map(send_one,
               [(email, pdf, event, ctype) for email, pdf in recipients])
