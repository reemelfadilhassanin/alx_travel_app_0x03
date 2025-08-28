from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Your booking (ID: {booking_id}) has been confirmed."
    from_email = "no-reply@yourdomain.com"
    send_mail(subject, message, from_email, [to_email])
