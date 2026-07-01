from django.shortcuts import render, redirect, get_object_or_404

from accounts.permissions import permit_creating, permit_updating, permit_deleting
from .forms import ProductForm
from .models import Product

# Create your views here.

def search_product(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(title__icontains = query)
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'product/list.html', context)

def get_product(request):
    products = Product.objects.all().order_by('-price')
    return render(request, 'product/list.html',{'products':products})

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



@permit_creating
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get-product')
    else:
        form = ProductForm()
    return render(request, 'product/create.html', {'form':form})

def read_product(request, pk=None):
    pro = Product.objects.get(pk = pk)
    return render(request,'product/read.html',{'pro':pro})

@permit_updating
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('get-product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update.html', {'form':form})

@permit_deleting
def delete_product(request, pk):
    pro = Product.objects.get(pk=pk)
    if request.method == 'POST':
        pro.delete()
        return redirect('get-product')
    else:
        return render(request,'product/delete.html',{'pro':pro})