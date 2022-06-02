from csv import list_dialects
from re import search
from django.contrib import admin
# from ckeditor.widgets import CKEditorwidget

# Register your models here.
from .models import *
from django.forms import ModelForm, CharField


# class ProductAdminForm(ModelForm):
#     description = CharField(widget=CkeditorWidget())
#     class Meta:
#         model = Product
#         field = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id']
    prepopulated_fields = {"slug":('name',)}


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = (
        'name', 
        'category', 
        'slug',
        'id'
        )
    prepopulated_fields = {"slug":('name',)}
    list_filter = (
        "category",
    )
    search_fields = (
        "id",
        "name",
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active'
    ]



@admin.register(BanerImage)
class BanerImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_link', 'image', 'created']
    list_filter = ['created']
    