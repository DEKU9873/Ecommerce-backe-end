from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import *



@api_view(['POST'])
def registeation_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            accont = serializer.save()

            data['response'] = "Successfully registered a new user"
            data['username'] = accont.username
            data['email'] = accont.email
            token = Token.objects.get(user=accont).key  
            data['token'] = token

        else:
            data = serializer.errors
            
            
        return Response(data) 
