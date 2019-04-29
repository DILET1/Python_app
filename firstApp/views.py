from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
# Create your views here.


def index(request):
    # return HttpResponse('Here is my response')
    return render(request, 'firstApp/index.html')


def about(request):
    return render(request, 'firstApp/about.html')


def kewlWebsites(request):
    coolwebs = []
    coolwebs.append('WarThunder')
    coolwebs.append('https://www.warthunder.net')
    coolwebs.append('Google.org')
    coolwebs.append('https://google.org')
    coolwebs.append('Amazon')
    coolwebs.append('amazon.com')
    return render(request, 'firstApp/kewlWebsites.html', coolwebs)


def form(request):
    return render(request, 'firstApp/form.html')


def greet(request):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    name = first_name + ' ' + last_name
    return render(request, 'firstApp/greet.html', {'name': name})


def login(request):
    logincreds = Login.objects.all()
    data_dict = dict()
    data_dict['logincreds'] = logincreds
    return render(request, 'firstApp/form', data_dict)
