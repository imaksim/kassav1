from django.urls import path
from calc import views

urlpatterns = [
    path("product/", views.ProductsListView.as_view(), name="products_view"),
    path("product-create-view/", views.ProductCreateAndListView.as_view(), name="products_create_view")


]
