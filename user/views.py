from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from user.models import UserProfile
from .forms import *
# Create your views here.

def loginPage(request):
    category = Category.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userProfile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userProfile.image.url
            messages.success(request,'Login Successfully')
            return redirect('/')
        else:
            messages.warning(request,'Username or Password is incorrect!')
            return redirect('/login')

    context = {'category':category}
    return render(request,'user/login_page.html',context)

def logOutPage(request):
    logout(request)
    return redirect('login')

def signupPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="img/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return redirect('/')
        else:
            messages.warning(request,form.errors)
            return redirect('/signup')


    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'user/signup_page.html', context)


def UserPage(request):
    return HttpResponse('<h1>This is User Page</h1>')

