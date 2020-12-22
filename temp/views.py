from django.shortcuts import render, redirect
from .models import Temperature
# from .forms import StudentForm, BookForm, IssueForm
from django.http import Http404, HttpResponseForbidden, JsonResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

def temp_get(request):
    if 'from' in request.GET and 'to' in request.GET:
        temp_data= Temperature.objects.filter(time__gte=request.GET['from'], time__lte=request.GET['to'])
    elif 'from' in request.GET:
        temp_data= Temperature.objects.filter(time__gte=request.GET['from'])
    elif 'to' in request.GET:
        temp_data= Temperature.objects.filter(time__lte=request.GET['to'])
    else:
        temp_data= Temperature.objects.all()
    data = serializers.serialize('json', list(temp_data), fields=('sensor_id','temperture','time'))
    return JsonResponse(data, safe=False)
        # if profile.user_type=='LIB':
        #     if request.method == 'POST':
        #         form = StudentForm(request.POST)
        #         if form.is_valid():
        #                 form.save()
        #                 return redirect('hello')
        #         else:
        #             return render(request, 'student.html', {"form":form}, status=400)
        #     else:
        #         form = StudentForm()
        #         return render(request, 'student.html', {"form":form}, status=200)
        # else:   
        #     return HttpResponseForbidden("You are not authorized to view this.")
def temp_post(request):
    
    json_data=json.loads(request.body.decode("utf-8"))
    print(json_data)
    try:
        Temperature.objects.create(
            sensor_id=int(json_data["sensor_id"]),
            time=json_data["time"],
            temperature=int(json_data["temperature"])
        )
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    return JsonResponse({})