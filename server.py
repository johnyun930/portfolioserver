from email import message
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
from message import send_email_to_me, send_attached_email


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/message", methods=["Post"])
@cross_origin()
def postmessage():
    data = request.json
    html = Template(Path('./index.html').read_text()).substitute(
        {'name': data["firstname"].capitalize(), "message":
         """
I really appreciate to leave your contact information for me.  
I will contact you as soon as possible
I also attached my resume with this email.


Sincerely,

        
John JongHun Yun"""})
    body = MIMEText(html, 'html')
    send_attached_email(data["email"], body)

    mymessage = Template(Path('./contact.html').read_text()).substitute({
        'firstname': data["firstname"],
        'lastname': data["lastname"],
        'email': data['email'],
        'phone': data['phone'],
        'message': data['message']
    })
    send_email_to_me(mymessage)
    return json.dumps(True)
