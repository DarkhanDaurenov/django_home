from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailsView, ProductCreateView, ProductUpdateView, \
ProductDeleteView, ContactView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailsView.as_view()), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
