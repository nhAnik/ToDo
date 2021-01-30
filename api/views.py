from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverView(request):
  api_urls = {
    'List':'/tasks/',
    'Detail View':'/tasks/<int:pk>/',
  }
  return Response(api_urls)


@api_view(['GET', 'POST'])
def taskList(request):
  if request.method == 'GET':
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def taskDetail(request, pk):
  try:
    task = Task.objects.get(id=pk)
  except Task.DoesNotExist:
    return HttpResponse(status=404)
  
  if request.method == 'GET':
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    task.delete()
    return Response("Successfully deleted!")
