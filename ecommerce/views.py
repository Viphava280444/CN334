from django.shortcuts import render
from django.http import HttpResponse

def ecommerce_index_view(request):

    return HttpResponse('Welcome to 6410742495 Viphava Khlaisuwan views!')

# Create your views here.
def item_view(request, item_id):
    contexts = {
        "item_id": item_id

    }
    return render(request, 'index.html', context= contexts)

def home_page(request):
    return render(request, 'home.html')

def category_page(request):
    return render(request, "category.html")

def product_page(request):
    return render(request, 'product.html')

def checkout_page(request):
    return render(request, 'checkout.html')

def contact_page(request):
    return render(request, 'contact.html')