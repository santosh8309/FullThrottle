import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from testapp.models import *

# Create your views here.

def combine(users, activityperiods):
    data = []
    for user in users:
        print('user', user)
        user = user['fields']
        uid = user['uid']
        for activity in activityperiods:
            activity = activity['fields']
            if activity['uid'] == uid:
                temp = user
                temp.update(activity)
                temp['id'] = temp['uid']
                del temp['uid']
                data.append(temp)
                break
    return data

def index(request):
    # get this data from the Models
    users = User.objects.all()
    users = serializers.serialize('json', users)
    activityperiods = ActivityPeriod.objects.all()
    activityperiods = serializers.serialize('json', activityperiods)

    # join both the json in the required format
    users = json.loads(users)
    activityperiods = json.loads(activityperiods)
    data = combine(users, activityperiods)

    final = {'ok': True, 'members': data}
    final = json.dumps(final, indent=4)
    return HttpResponse(final, content_type="application/json")
