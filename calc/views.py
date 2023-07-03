from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from calc.models import Stuff, Products, PaymentMethods,Operations,Sales
from .forms import ProductForm, StuffForm
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
        if 'delete_selected' in request.POST:
            selected_items = request.POST.getlist('selected_item')
            print(request.POST, selected_items)
            Products.objects.filter(id__in=selected_items).delete()
            return redirect(self.request.path_info)
        elif 'add_item' in request.POST:
            form = self.get_form()
            print(form)
            return self.form_valid(form)
            # return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StuffCreateAndListView(CreateView, ListView):
    model = Stuff
    template_name = 'calc/stuff_create.html'
    form_class = StuffForm
    context_object_name = 'stuff_list_create'
    success_url = reverse_lazy('stuff_create_view')
    def post(self, request, *args, **kwargs):
        if 'stuff_selected' in request.POST:
            selected_items = request.POST.getlist('stuff_selected')
            print(request.POST, selected_items)
            Stuff.objects.filter(id__in=selected_items).delete()
            return redirect(self.request.path_info)
        elif 'add_item' in request.POST:
            form = self.get_form()
            print(form)
            return self.form_valid(form)


            # return super().post(request, *args, **kwargs)



