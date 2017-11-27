import json
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from api.models import AppInfo
from api.models import UserInfo

def index(request):
    return JsonResponse({'status':'OK'})

@csrf_exempt
def app(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        app_name = data["name"]
        app_email = data["email"]
        app_type = data["type"]
        if app_name != "" and app_email != "" and app_type != "":
            a_info = AppInfo(app_name=app_name,app_email=app_email,app_type=app_type)
            a_info.save()
            token = hashlib.sha1("%sand%s"%(app_name,app_email)).hexdigest()
            return JsonResponse({'token':token})
        else:
            return JsonResponse({'status':'ERROR'})
    elif request.method == 'GET':
        return JsonResponse({'status':'ERROR'})

@csrf_exempt
def user(request):
    if request.method == 'POST':
        return JsonResponse({'status':'OK'})
    elif request.method == 'GET':
        return JsonResponse({'status':'ERROR'})

@csrf_exempt
def data(request):
    if request.method == 'POST':
        return JsonResponse({'status':'OK'})
    elif request.method == 'GET':
        return JsonResponse({'status':'ERROR'})
