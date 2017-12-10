import hashlib
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import AppInfo
from api.models import UserInfo
from api.models import LocationData


def index(request):
    return JsonResponse({'status': 'OK'})


@csrf_exempt
def app(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        app_name = data["name"]
        app_email = data["email"]
        app_type = data["type"]
        if app_name != "" and app_email != "" and app_type != "":
            token = hashlib.sha1(("%sand%s" % (app_name, app_email)).encode('utf-8')).hexdigest()
            a_info = AppInfo(app_name=app_name, app_email=app_email, app_type=app_type, app_key=token)
            a_info.save()
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'status': 'ERROR'})
    elif request.method == 'GET':
        return JsonResponse({'status': 'ERROR'})


@csrf_exempt
def user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_name = data["name"]
        user_email = data["email"]
        user_phone = data["phone"]
        if user_name != "" and (user_email != "" or user_phone != ""):
            token = hashlib.sha1(("%sand%sand%s" % (user_name, user_email, user_phone)).encode('utf-8')).hexdigest()
            user_info = UserInfo(user_name=user_name, user_email=user_email, user_phone=user_phone, user_key=token)
            user_info.save()
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'status': 'ERROR'})
    elif request.method == 'GET':
        return JsonResponse({'status': 'ERROR'})


@csrf_exempt
def data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        location_name = data["name"]
        location_type = data["type"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        altitude = data["altitude"]
        app_key = data["appKey"]
        user_key = data["userKey"]
        if latitude != "" and longitude != "" and app_key != "" and user_key != "":
            location_data = LocationData(location_name=location_name, location_type=location_type,
                                         latitude=latitude, longitude=longitude, altitude=altitude,
                                         app_key=app_key, user_key=user_key)
            location_data.save()
            return JsonResponse({'status': 'OK'})
    elif request.method == 'GET':
        return JsonResponse({'status': 'ERROR'})
