from rest_framework import serializers
from ..models.category_model import Category
from ..models.product_model import Product
from django import forms
from user_app.serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User


# Rest framework support HyperlinkedModelSerializer, Serializer, ModelSerializer, ListSerializer
class CategorySerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = UserSerializer(required=True)

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['id', 'title', 'code', 'image', 'content', 'active', 'user']


class CategoryAddSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # product_map = serializers.StringRelatedField(read_only=True)
    user = UserSerializer
    product_map = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select
    )

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['title', 'code', 'image', 'content', 'user']
