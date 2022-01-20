from django.shortcuts import redirect, render
from .models import songs

# Create your views here.
def index(request):

    
    coll = songs.objects.all()


    return render(request, 'index.html', {'coll' : coll})


passer = []
def pop(request):

    coll = songs.objects.all()

    for colls in coll :
        if colls.genre == 'pop':
            passer.append(colls)
    return render(request, 'pop.html', {'coll' : passer})


def search(request):
    flag = 0
    coll = songs.objects.all()

    search_string = request.POST['search-bar']

    for colls in coll :
        if(colls.name == search_string):
            passer.append(colls)
            flag = 1

    return render(request, 'index.html',{'search': passer, 'coll' : coll})