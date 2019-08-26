from django.shortcuts import render, redirect  
from Storage.forms import ProductForm
from Storage.models import Product
# Create your views here.  
def vendi(request):
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form})  
def edit(request, id):
    product = Product.objects.filter(pid=id)
    #Product = Product.objects.get()
    return render(request,'edit.html', {'Product':product})
def show(request):
    Products = Product.objects.all()
    for p in Products:
        print(p.name)
    return render(request,"show.html",{'Products':Products})
def update(request, id):
    product = Product.objects.get(pid=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'Product': product})
def destroy(request, id):  
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/show")

