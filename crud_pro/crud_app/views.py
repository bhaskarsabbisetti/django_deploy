from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .seralizers import DeploySerializer
# Create your views here.
def grettings(req):
    return HttpResponse("hello user welcom to our site")
@csrf_exempt
def register(req):
    if req.method=="POST":
        # data=req.POST.dict()
        data=json.loads(req.body)
        seralize=DeploySerializer(data=data)
        if seralize.is_valid():
            seralize.save()
            return HttpResponse('user created')
        else:
            # return HttpResponse('failed to register')
            print("Validation errors:",seralize.errors)
            return JsonResponse(seralize.errors, status=400)
    
    return JsonResponse({"message": "Only POST allowed"}, status=405)
