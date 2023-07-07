from django.shortcuts import render
from django.contrib.auth.models import User



def index(request):
    users = User.objects.all()
    return render(request, 'home/home.html', context={"users": users})


def get_user(request, id):
    user = User.objects.get(id=id)
    return render(request, 'home/user.html', context={'user': user})


def save_user(request, id):
    print(request.POST)
    data = request.POST
    print(data.get('id'))
    print(data.get('username'))
    print(data.get('email'))
    User.objects.filter(id=data.get('id')).update(username=data.get('username'),
                                                          email=data.get('email'),
                                                         )
    users = User.objects.all()
    return render(request, 'home/home.html', context={"users": users})

