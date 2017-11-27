import json
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
        name = data["name"]
        email = data["email"]
        app_type = data["type"]
        print name
        print email
        print app_type
        if name != "" and email != "" and app_type != "":
            a_info = AppInfo(app_name=name,app_email=email,app_type=app_type)
            a_info.save()
            return JsonResponse({'status':'OK'})
        else:
            return HttpResponse(request.body)
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
