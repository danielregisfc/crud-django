from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


@api_view(['GET','POST'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(request.META)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)
       
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def get_users_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)



    