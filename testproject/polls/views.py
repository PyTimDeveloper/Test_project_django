from django.shortcuts import render

def index(request):
  return render(request, 'My blog/index.html')