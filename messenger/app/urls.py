from django.urls import path
from . import views

urlpatterns = [
	path('user-registration/', views.UserRegistration.as_view(), name='user-registration'),
	path('verify-user/', views.VerifyUser.as_view(), name='verify-user'),
]