from django.shortcuts import render

# Create your views here.


def index(request):
    fav1 = 'Aviation'
    fav2 = 'FPS games'
    fav3 = 'Confucianist people'
    fav4 = 'Dilet'
    fav5 = 'Naniism'
    return render(request, 'index.html', {'fav1': fav1, 'fav2': fav2, 'fav3': fav3, 'fav4': fav4, 'fav5': fav5, 'admin': False, 'member': False})


def name_form(request):
    return render(request, 'firstApp/form.htmlS')
