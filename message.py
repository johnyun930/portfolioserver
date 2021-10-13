import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import dotenv_values
config = dotenv_values(".env")


def send_email(email):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(config["EMAIL"], config["PASSWORD"])
        smtp.send_message(email)


def send_email_to_me(html):
    email = EmailMessage()
    email['from'] = "MySelf"
    email['to'] = "johnyunwork@gmail.com"
    email['subject'] = "Someone sent you message through your website"
    email.set_content(html, 'html')
    send_email(email)


def send_attached_email(recevier, html):
    email = MIMEMultipart()
    email['from'] = 'John Jonghun Yun'
    email['to'] = recevier
    email['subject'] = "Thank you for reaching out to me"

    email.attach(html)

    resume = MIMEApplication(open("JongHunYun_Resume.pdf", "rb").read())
    resume.add_header('Content-Disposition', 'attachment',
                      filename="JongHunYun_Resume.pdf")
    email.attach(resume)
    send_email(email)
