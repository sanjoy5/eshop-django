from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from django.contrib import messages

# Create your views here.

def category_products(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    category_name = Category.objects.get(id=id)

    context = {'products':products,'category':category,'category_name':category_name}
    return render(request,'product/category_products.html',context)


def product_details(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    comment = Comment.objects.filter(product_id=id,status=True)
  
    images = Images.objects.filter(product_id=id)
    context = {
        'product':product,
        'category':category,
        'images':images,
        'comment':comment,
   
        }
    return render(request,'product/product_details.html',context)


def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']

            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)
            
            category = Category.objects.all()
            context = {'products':products,'category':category,'query':query}
            return render(request,'product/search_product.html',context)
    return redirect('/')
        
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def search_auto(request):
    if is_ajax(request=request):
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title 
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

    

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            data.user_id = request.user.id
            data.save()
            messages.success(request," Thank you for your Review.")
            return redirect(url)

    return redirect(url)