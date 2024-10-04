from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request):
    context = {
        'name' : 'jacky',
        'location': 'sky',
        'story' : 'jack'
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method=='POST':
        fn = request.POST['fname']
        email = request.POST['email']
        passw = request.POST['pass']
        rp = request.POST['rp']
        
        if passw == rp:
            if User.objects.filter(email=email):
                messages.info(request, 'Email already Used')
                return redirect('register')
               
            elif User.objects.filter(fn=fn).exists():
                messages.info(request, 'Username already Used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(fn=fn, email=email, password=passw)
                user.save()
                return redirect('login')
        
        
        else:
            messages.info(request, 'Password not same')
            return redirect('register')   
            
    return render(request, 'register.html')        
            
        


def count(request):
    text = request.POST['text']
    return render(request, 'count.html', {'text':text})
    