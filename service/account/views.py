from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from .tasks import send_feedback_email_task

@api_view(['POST' ,])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['email'] = user.email
            data['username'] = user.username
            print(user.email, user.username)
            return Response(data, status=status.HTTP_201_CREATED)
        

        data = serializer.errors

        return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
    
    