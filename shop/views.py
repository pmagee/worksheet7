from django.views.generic import ListView
from .models import Product, Category

class ProductListView(ListView):
    model =  Product
    template_name = 'home.html'
    context_object_name = 'all_products_list'


    def categories(self):
        return Category.objects.all()

