from django.shortcuts import render

# Create your views here.
def index(request):
    products = products.objects.all()
    return render(request, 'products/index.html', {'products': products})