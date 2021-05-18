from celery import shared_task

from django.template.loader import render_to_string
from sendgrid import Mail, SendGridAPIClient

from LMS.settings import SENDGRID_KEY, EMAIL_SENDER
from logger.models import Log


@shared_task
def send_email(data):
    context = {
        'name': data['name'],
        'email': data['email'],
        'message': data['text_message']
    }
    content = render_to_string('mail/get_message.html', context)
    message = Mail(
        from_email=EMAIL_SENDER,)
    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message)
    print("Send message")
    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message)
    print("Send message")


@shared_task
def clear_log():
    Log.objects.all().delete()
