from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage

def products_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Product.objects.create(
                name=data['name'],
                description=data['description'],
                price=data['price'],
                quantity=data['quantity'],
                product_registration_date=data['product_registration_date'],)
            image = data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)


            return redirect('products_form')
    else:
        form = ProductForm()
    return render(request, 'task1_app/product_form.html', {'form': form})

def products_days_filter(request, days):
    now = datetime.now().date()
    search_date = now - timedelta(days=days)

    products = Product.objects.filter(product_registration_date__range=[search_date, now])
    return render(request, 'task1_app/products.html', {'products':products})