from django.shortcuts import render
from django.views.generic import ListView
from taggit.models import Tag
from .models import Product
# Create your views here.
from django.views.generic import ListView
from .models import Product

class ProductView(ListView):
    template_name = "index.html"
    context_object_name = "data"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(status="PB")




def Search_Tag(request , tag):
    tag = tag
    tag = Tag.objects.get(name__exact=tag)
    post = Product.objects.filter(tag__exact=tag)
    return render(request , "list_tag.html" , {"data" :post , "tag" : tag })
def Detail_Product(request , pk , name):
    data = Product.objects.get(pk=pk)
    Similar = Product.objects.filter(tag__in=data.tag.all()).exclude(id=data.id)
    print(Similar)
    return render(request , "detail.html" , {"data" : data , "similar":Similar})