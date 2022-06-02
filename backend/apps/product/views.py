from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from django.db.models import Q

from django_filters.views import FilterView

import json
# Create your views here.
from .models import SubCategory, Category, Product, BanerImage


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baners = BanerImage.objects.all()
        if len(baners) > 6:
            baners = baners[:6]
        context['baners'] = baners
        return context


from .filters import ProductFilter
class ProductListView(FilterView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 3
    filterset_class = ProductFilter

    # стандартное имя списка продуктов в шаблоне
    # для ListView - object_list

    def get_queryset(self):
        print(self.kwargs)
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        print(category_slug)
        print(subcategory_slug)
        if subcategory_slug:
            products = Product.objects.filter(is_active=True, subcategory__slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"  # стандартный object


class ProductSearchView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10

    def get_queryset(self):
        search_text = self.request.GET.get("query")
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            | Q(description__icontains=search_text)
        )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get("query")
        return context
