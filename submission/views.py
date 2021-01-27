#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.conf import settings

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        data = json.loads(request.POST['json'])
        try:
            idle_time = data['idle_time']
            #process the json data

        except KeyError:
            HttpResponseServerError("Malformed data!")

        dir = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(dir, exist_ok=True)
        json_path = os.path.join(dir,'file.json')
        with open(json_path, 'w') as f:
            json.dump(data, f)

    else:
        return HttpResponseNotFound()

    return HttpResponse("Got json data")
