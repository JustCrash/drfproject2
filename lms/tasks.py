from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription
from users.models import User


@shared_task
def send_mail_about_updates(course_id):
    """
    Отправка писем об обновлении курса.
    """
    subs = Subscription.objects.filter(course=course_id)
    subscribers_email = []
    for sub in subs:
        subscribers_email.append(User.objects.get(pk=sub.user.pk).email)
        course = sub.course
        user = sub.user
        send_mail(
            subject=f'{course} обновился',
            message=f'{course} обновился',
            from_email=EMAIL_HOST_USER,
            recipient_list=subscribers_email,
            fail_silently=False
        )
        print(f'Письмо отправлено пользователю {user.email}')
