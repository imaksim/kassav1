from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from calc.models import Stuff, Products, PaymentMethods,Operations,Sales
from .forms import ProductForm
# Create your views here.

class ProductsListView (ListView):
    model = Products
    template_name = 'calc/products_create_form.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'calc/product_create_form.html'
    context_object_name = 'product_create'
    success_url = reverse_lazy('products_create_form')


class ProductCreateAndListView(CreateView, ListView):
    model = Products
    template_name = 'calc/products_create.html'
    form_class = ProductForm
    context_object_name = 'product_list_create'
    success_url = reverse_lazy('products_create_view')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'selected_item' in request.POST:
            selected_items = request.POST.getlist('selected_item')
            Products.objects.filter(id__in=selected_items).delete()

        return super().post(request, *args, **kwargs)





