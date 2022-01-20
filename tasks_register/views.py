from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerialzer

@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET': # tasks requesting data 
        snippets = Task.objects.all()
        serializer = TaskSerialzer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # tasks posting data
        serializer = TaskSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
