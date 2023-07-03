import debug_toolbar
from django.urls import include, path
from calc import views


urlpatterns = [
    path("product/", views.ProductsListView.as_view(), name="products_view"),
    path("product-create-view/", views.ProductCreateAndListView.as_view(), name="products_create_view"),
    path("product-create-form/", views.ProductCreateView.as_view(), name="products_create_form"),
    path('_debug/', include(debug_toolbar.urls)),

]




