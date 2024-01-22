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