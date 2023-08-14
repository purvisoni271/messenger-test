from django.conf import settings
from twilio.rest import Client

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN


def send_otp(mobile_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="OTP for verfiy your mobile number: "+otp,
                     from_='+15188568884',
                     to='+91' + mobile_number
                 )
    print(message.sid)
