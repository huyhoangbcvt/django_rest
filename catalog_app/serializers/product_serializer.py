from rest_framework import serializers
from ..models.product_model import Product
from ..serializers.category_serializer import CategorySerializer
from user_app.serializers.user_serializer import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=True)
    # categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'p_name', 'p_code', 'p_image', 'p_description', 'p_country', 'active', 'user', 'categories']


class ProductAddSerializer(serializers.ModelSerializer):
    # categories = serializers.PrimaryKeyRelatedField(queryset=Product.objects.prefetch_related('catalog_products'))
    user = UserSerializer
    categories = CategorySerializer

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['p_name', 'p_code', 'p_image', 'p_description', 'p_country', 'user', 'categories']
