from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'


class ContactView(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_picture', 'product_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_picture', 'product_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')