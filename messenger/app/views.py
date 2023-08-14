import random
import string
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from .models import Profile
from .serializer import ProfileSerializer
from .utils import *

from rest_framework.response import Response
from rest_framework import status


class UserRegistration(APIView):
    """
    User Registration API
    """

    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']
            gender = request.data['gender']
            mobile_number = request.data['mobile_number']
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=email)
            return Response({'message': 'User already registered!!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            user = User.objects.create(username=email,
                                       email=email,
                                       first_name=first_name,
                                       last_name=last_name,
                                       password=password)
            otp = ''.join(random.choice(string.digits) for _ in range(4))
            send_otp(mobile_number, otp)
            profile = Profile.objects.create(user=user,
                                             otp=otp,
                                             gender=gender,
                                             mobile_number=mobile_number)
            return Response({'message': 'User successfully registered!!'}, status=status.HTTP_201_CREATED)


class VerifyUser(APIView):
    """
    Veriy User API
    """
    
    def post(self, request, format=None):
        data = request.data
        try:
            email = request.data['email']
            otp = request.data['otp']
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=email)
            profile = Profile.objects.get(user=user)
            if profile.otp == otp:
                profile.is_verify = True
                profile.save()
                return Response({'message': 'OTP verified!!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid OTP!!'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            
            return Response({'message': 'User successfully registered!!'}, status=status.HTTP_201_CREATED)
