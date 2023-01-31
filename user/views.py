from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import *
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib import messages
from user.models import UserProfile
from order.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
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

@login_required(login_url='/login')
def UserPage(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile':profile,'category':category}
    return render(request,'user/user_profile.html',context)
    



@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user/user_update.html', context)



@login_required(login_url='/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/user')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'user/user_password.html', {'form': form,'category':category})


@login_required(login_url='/login')
def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'orders': orders,'category':category}
    return render(request, 'user/user_orders.html', context)


@login_required(login_url='/login')
def user_orderdetail(request, id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        'order': order,
        'orderitems': orderitems,
        'category':category
    }
    return render(request, 'user/user_order_detail.html', context)


@login_required(login_url='/login')
def user_order_product(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(
        user_id=current_user.id).order_by('-id')
    context = {'order_product': order_product,'category':category}
    return render(request, 'user/user_order_products.html', context)


@login_required(login_url='/login')
def user_order_product_detail(request, id, oid):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {
        'order': order,
        'orderitems': orderitems,
        'category':category
    }
    return render(request, 'user/user_order_detail.html', context)