import threading
from threading import Thread
from django.conf import settings
from django.core.mail import send_mail

class EmailThread(threading.Thread):
    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.message = message
        threading.Thread.__init__(self)

    def run (self):
        send_mail(self.subject,self.message,settings.EMAIL_HOST_USER,self.recipient_list,fail_silently=False)

def send_html_mail(subject, message, recipient_list):
    EmailThread(subject, message, recipient_list).start()