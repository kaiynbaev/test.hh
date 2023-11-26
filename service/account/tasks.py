from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_feedback_email_task(email_address, username):
    """Sends an email when the feedback form has been submitted."""  # а когда не делали
    send_mail(
        "user was succesfully register",
        f"\t{username}\n\nThank you!",
        "django application with celery",
        email_address,
        fail_silently=False,
    )
    print('otrabotal')
    