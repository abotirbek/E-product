from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def get_product(request):
    pro = Product.objects.all().order_by('-price')
    return render(request, 'product/list.html',{'pro':pro})

def get_over_500(request):
    pro = Product.objects.filter(price__gte=500).order_by('price')
    return render(request, 'product/list.html', {'pro': pro})

def get_first(request):
    pro = Product.objects.first()
    return render(request, 'product/read.html',{'pro':pro})

def get_last(request):
    pro = Product.objects.last()
    return render(request, 'product/read.html',{'pro':pro})

def get_reverse(request):
    pro = Product.objects.reverse()
    return render(request,'product/list.html',{'pro':pro})

def count_products(request):
    quantity = Product.objects.count()
    return render(request, 'product/data.html',{'quantity':quantity})

def check_existence(request):
    existence = Product.objects.exists()
    return render(request,'product/data.html',{'existence':existence})

def get_none(request):
    none = Product.objects.none()
    return render(request,'product/data.html',{'none':none})

def get_distinct(request):
    pro = Product.objects.distinct()
    return render(request,'product/list.html',{'pro':pro})

def get_dict(request):
    pro_dict = Product.objects.values()
    return render(request,'product/data.html',{'pro_dict':pro_dict})

def get_tuple(request):
    pro_tuple = Product.objects.values_list()
    return render(request,'product/data.html',{'pro_tuple':pro_tuple})

def get_list(request):
    pro_list = Product.objects.values_list('title',flat=True)
    return render(request,'product/data.html',{'pro_list':pro_list})

def get_only(request):
    pro_only = Product.objects.only('title','price')
    return render(request,'product/data.html',{'pro_only':pro_only})

def defer(request):
    pro_defer = Product.objects.defer('created_at')
    return render(request,'product/data.html',{'pro_defer':pro_defer})

def get_iterator(request):
    pro_iterator = Product.objects.defer('created_at')
    return render(request,'product/data.html',{'pro_iterator':pro_iterator})

def get_raw(request):
    pro_raw = Product.objects.raw('select * from product_product where price > 1000')
    return render(request,'product/data.html',{'pro_raw':pro_raw})

def get_specific_price(request):
    pro = Product.objects.filter(price__exact=200)
    return render(request,'product/read.html',{'pro':pro})




















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
        updated_at = request.POST.get('updated_at',pro.updated_at)
        if title and price and quantity and description and updated_at:
            pro.title = title
            pro.price = price
            pro.quantity = quantity
            pro.description = description
            pro.updated_at = updated_at
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