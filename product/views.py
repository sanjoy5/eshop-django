from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json

# Create your views here.

def category_products(request,id,slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    category_name = Category.objects.get(id=id)

    context = {'products':products,'category':category,'category_name':category_name}
    return render(request,'product/category_products.html',context)


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

    