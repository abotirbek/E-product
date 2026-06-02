from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def get_product(request):
    pro = Product.objects.all()
    return render(request, 'product/list.html',{'pro':pro})

def create_product(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        if title and price and quantity and description:
            Product.objects.create(
                title = title,
                price = price,
                quantity = quantity,
                description = description,
            )
            return redirect('create')
    else:
        return render(request, 'product/create.html')

def read_product(request, pk=None):
    pro = Product.objects.get(pk = pk)
    return render(request,'product/read.html',{'pro':pro})

def update_product(request, pk):
    pro = Product.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get('title',pro.title)
        price = request.POST.get('price',pro.price)
        quantity = request.POST.get('quantity',pro.quantity)
        description = request.POST.get('description',pro.description)
        if title and price and quantity and description:
            pro.title = title
            pro.price = price
            pro.quantity = quantity
            pro.description = description
            pro.save()
            return redirect('get-product')
    else:
        return render(request,'product/update.html',{'pro':pro})


def delete_product(request, pk):
    pro = Product.objects.get(pk=pk)
    if request.method == 'POST':
        pro.delete()
        return redirect('get-product')
    else:
        return render(request,'product/delete.html',{'pro':pro})

def search_product(request, title=None):
    pro = Product.objects.get(title = title)
    return render(request,'product/read.html',{'pro':pro})