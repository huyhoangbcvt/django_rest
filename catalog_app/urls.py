from .modules import views_catalog
from .modules import views_product
from .modules import views_category, views_product
from django.urls import path, include

# determine the name from the viewset, as it does not have a `.queryset` attribute.
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'category', views_category.CategoryInfoViewSet, basename="category_list")
# router.register(r'product', views_product.ProductInfoViewSet, basename="product_list")
app_name = 'catalog'

urlpatterns = [
    # path('', views_catalog.index, name='index'),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Rest Framework
    # Category
    path("category/", views_category.GetCategoryInfo, name="category_list"),
    path("category/add/", views_category.AddCategory, name="category_add"),
    path("category/create/", views_category.CreateCategory.as_view(), name="create_category"),
    # path('category/view/<int:pk>/', None, name='category_detail'),
    # Product
    path("product/", views_product.GetProductInfo, name="product_list"),
    path("product/add/", views_product.AddProduct, name="product_add"),
    path("category/create/", views_product.CreateProduct.as_view(), name="create_product"),
    # path('category/view/<int:pk>/', None, name='product_detail'),

]