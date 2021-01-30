from django.shortcuts import render

def listView(request):
  context = {}
  return render(request, 'frontend/list.html', context)
