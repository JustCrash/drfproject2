from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription
from users.models import User
from lms.models import Course


@shared_task
def send_mail_about_updates(course_id: int) -> None:
    """
    Отправка писем об обновлении курса.
    """
    course = Course.objects.get(pk=course_id)
    recipients = Subscription.objects.filter(course=course).values_list(
        'user__email', flat=True)

    send_mail(
        subject=f'{course.title} обновился',
        message=f'курс - {course.title} - обновился',
        from_email=EMAIL_HOST_USER,
        recipient_list=list(recipients),
        fail_silently=False
    )
