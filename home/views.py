from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from product.models import Category,Product

# Create your views here.

def home(request):

    setting = Setting.objects.get(id=1)
    slider_imgs = SliderImage.objects.all().order_by('-id')
    category = Category.objects.all()
    latest_product = Product.objects.all().order_by("-id")
    random_product = Product.objects.all().order_by("?")
    
    page = "home"
    context = {'setting':setting,'page':page,'category':category,'slider_imgs':slider_imgs,'latest_product':latest_product,"random_product":random_product}
    return render(request,'home/index.html',context)

def aboutPage(request):
    setting = Setting.objects.get(id=1)
    context = {'setting':setting}
    return render(request,'home/about.html',context)


def contactPage(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Your message has been sent. Thank you for your message.")
            return redirect('/contact')
    setting = Setting.objects.get(id=1)
    context = {'setting':setting,'form':form}
    return render(request,'home/contact.html',context)


