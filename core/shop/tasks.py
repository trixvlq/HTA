from celery import shared_task
from decouple import config
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Cart


@shared_task
def delete_old_carts_task():
    threshold = timezone.now() - timedelta(hours=24)
    Cart.objects.filter(updated_at__lt=threshold).delete()


@shared_task
def checkout_cart(message, email=config('HOME_EMAIL')):
    send_mail(
        'Ваш заказ',
        message,
        config('EMAIL'),
        [email],
    )
