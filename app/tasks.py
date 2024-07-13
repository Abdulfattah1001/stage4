from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
app = Celery('tasks', broker = "pyamqp://guest@localhost//")
logger = logging.getLogger('messaging_system')
logger.setLevel(logging.DEBUG)

app.config_from_object("celeryconfig")


@app.task
def add():
    return "Hello There"


@app.task
def sendMail(receiver):
    #server= 'smtp.gmail.com'
    #port = 587
    sender = "aminufattah6@gmail.com"
    password="dfzs phip tahr lhdl"
    subject="SMTP implementation"
    body="Hello greetings from HNG"
    message=MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    #message['Body'] = body
    message.attach(MIMEText(body,'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(sender,password)
            server.sendmail(sender,receiver,message.as_string())
            server.quit()
            return f"Email sent succesfully"
    except Exception as e:
        return f"Failed to send email to {receiver}. Error:{str(e)}"
    
@app.task
def logMessage():
    log_file = '/var/log/messaging_system.log'
    log_handler = logging.FileHandler(log_file)
    log_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.debug("Logged")
    return "Logging message"