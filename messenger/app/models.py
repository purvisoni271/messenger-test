from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICE = ((1, 'Male'), (2, 'Female'), (3, 'Other'))


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	otp = models.CharField(max_length=10)
	gender = models.IntegerField(choices=GENDER_CHOICE)
	mobile_number = models.CharField(max_length=12)
	is_verify = models.BooleanField(default=False)

	def __str__(self):
		return self.mobile_number


class Messages(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message_text = models.TextField()
