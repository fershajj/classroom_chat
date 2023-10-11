import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import otpgen

def pwreset(tomail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('emailid','password')  #enter emailid and password (if email id is a gmail id, create an app password for password)

    msg=MIMEMultipart()
    msg['From']='senders name' #enter sender's name
    msg['to']=tomail+'@gmail.com'
    msg['subject']='Reset Password'
    global otp
    otp=otpgen.main()
    message=f"Hello!\nYour OTP for password reset is {otp}"
    msg.attach(MIMEText(message,'plain'))

    text=msg.as_string()
    server.sendmail('senders email address',tomail+'@gmail.com',text) #enter sender's email id

def main(tomail):
    pwreset(tomail)
    return otp

    