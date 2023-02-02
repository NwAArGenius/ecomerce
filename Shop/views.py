from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from Cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


def home(request):
    produit = Product.objects.all()
    paginator = Paginator(produit,2)
    page_number = request.POST.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'produits':produit , 'page_obj':page_obj}
    return render(request,'products/home.html', context)

def detaisl_product(request,pk):
    produit = get_object_or_404(Product , id=pk)   
    form = CartAddProductForm()
    context={'produit':produit , "form":form}
    return render (request, 'products/detail.html',context)

  
