from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def create_product_view(request):
    my_form = ProductForm()
    if request.method == "POST":
        my_form = ProductForm(request.POST)
        
    print(my_form)
    context = {
        "my_form": my_form
    }
    return render(request, 'create_product.html', context)
    