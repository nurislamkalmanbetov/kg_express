# преобразовать данный из базы в json format

from rest_framework import serializers

from backend.apps.product.models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug'
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'slug',
            'category'
        ]


class ProductSerializer(serializers.ModelSerializer):
    # для более подробной информации : https://www.django-rest-framework.org/
    # category = CategorySerializer(read_only=True)
    # subcategory = SubCategorySerializer(read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    subcategory = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    class Meta:
        model = Product
        fields = '__all__'



class CategoryDetailSerializer(serializers.ModelSerializer):
    # subcategories = SubCategorySerializer(
    #     read_only=True,many=True
    # )

    subcategories = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name"
    )



    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']





