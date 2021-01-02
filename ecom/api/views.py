# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def info(request):
    return JsonResponse({'info': 'Django React App', 'name': "Abin"})
