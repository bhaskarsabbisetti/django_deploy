from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def grettings(req):
    return HttpResponse("hello user welcom to our site")
