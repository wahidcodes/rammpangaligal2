import random
from django.core.mail import send_mail
from .models import EmailOTP

def send_otp_via_email(username, email):
    otp = str(random.randint(100000, 999999))  # 6 digit OTP
    EmailOTP.objects.create(otp=otp, email=email)

    subject = "Your OTP Code"
    message = f"Hello {username},\n\nYour OTP is {otp}. It will expire in 5 minutes."
    from_email = "amwahid2004@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return otp