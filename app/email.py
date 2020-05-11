from flask_mail import Message
from . import mail
from flask import current_app
from flask import render_template

# Todo need reimplement
def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender='daoducnha2949301@gmail.com',
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    mail.send(msg)

