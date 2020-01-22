from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from ecommerce.models import UserProfile
# Create your views here.



from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        Name = request.POST['name']
        email = request.POST['email']
        First_Name = request.POST['FirstName']
        Last_Name = request.POST['LastName']
        Password1 = request.POST['pwd']
        Password2 = request.POST['pwd-confirm']
        user = User.objects.create_user(Name=name,email=email,First_Name=FirstName,Last_Name=LastName,Password1=pwd,Password2=pwd-confirm)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request, 'ecommerce/register.html')
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'ecommerce/login2.html', {})
    return render(request, 'ecommerce/login2.html', {})

def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'ecommerce/profile.html', {"query":query})
    else:
        return render(request, 'ecommerce/login2.html', {})


def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return render(request, 'ecommerce/login2.html', {})
