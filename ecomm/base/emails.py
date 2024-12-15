from django.conf import settings
from django.core.mail import send_mail

def send_activation_mail(email,email_token):
    link = f'http://127.0.0.1:8000/accounts/activate/{email_token}' 
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'pls click the link to activate: {link}'
    send_mail(subject, message,email_from,[email])