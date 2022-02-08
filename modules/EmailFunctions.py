import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

from modules import constants


class EmailFunctions(object):
    def __init__(self):
        context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        try:
            self.server.login(constants.EMAIL, constants.EMAIL_PASSWORD)
        except AttributeError:
            raise Exception('To perform login, you need to set environment '
                            'variables EMAIL and EMAIL_PASSWORD.')

    def send_email(self, to, attach, email_message=constants.DEFAULT_MESSAGE):
        """
        :param to: Email of user that you want to send email
        :param attach: Attachment path file.
        :param email_message: Message for body of your email, default is on
        constants.DEFAULT_MESSAGE.
        :return: Nothing because send_message method dont return anything
        to verify if email was successfully sent.
        """
        msg = EmailFunctions.get_attached_message(to, attach, email_message)
        self.server.send_message(msg, 'constants.EMAIL', to)

    @staticmethod
    def get_attached_message(to,
                             attach,
                             email_message=constants.DEFAULT_MESSAGE):
        """
        :param to: Email of user that you want to send email
        :param attach: Attachment path file.
        :param email_message: Message for body of your email, default is on
        constants.DEFAULT_MESSAGE.
        :return: Email message with attached file.
        """
        msg = MIMEMultipart()
        msg['From'] = constants.EMAIL
        msg['To'] = to
        msg['Subject'] = constants.DEFAULT_SUBJECT

        body = MIMEText(email_message, 'plain')
        msg.attach(body)

        with open(attach, 'rb') as f:
            filename = basename(attach)
            attachment = MIMEImage(f.read(), name=filename)

        msg.attach(attachment)
        return msg
