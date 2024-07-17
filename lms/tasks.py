import smtplib

from celery import shared_task
from django.core.mail import send_mail

from lms.models import Course
from users.models import User
from config import settings


@shared_task
def send_mail_about_updates(pk):
    """
    Отложенная задача. При обновлении курса отправляет
    письмо пользователю, подписанному на курс.
    """
    instance = Course.objects.filter(pk=pk).first()

    if instance:

        subscribers = instance.subscription_set.filter(cource=cource)
        subscribers_email = []
        for subscriber in subscribers:
            subscribers_email.append(User.objects.get(pk=subscriber.user.pk).email)

        try:
            send_mail(
                subject=f'Обновление курса {instance.name}',
                message=f'Информация курса {instance.name} обновилась, заходи на сайт, чтобы увидеть изменения!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=subscribers_email,
                fail_silently=False
            )
        except smtplib.SMTPException as error:
            raise error
