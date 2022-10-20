from django.db import models
from django.contrib.auth.models import User
# from .product_model import Product
from datetime import datetime
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/', null=True, default=None, blank=True)
    content = models.TextField(max_length=1000, null=True, default=None)
    created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    updated_at = models.DateTimeField(null=True, default=datetime.now, blank=True) # auto_now_add=True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product = models.ManyToManyField(Product, help_text='Select a Product for this Catalog')
    # product_map = models.PositiveSmallIntegerField(null=True, default=0, blank=True)
    active = models.BooleanField(
        _("post status"),
        default=True,
        help_text=_("Open - close status post with user"),
    )

    # Ko có cái này thì table tạo ra theo appname_classmodel
    # class Meta:
    #     managed = True
    #     db_table = 'catalogapp_catalog'
    class Meta:
        ordering = ['created_at', 'title']
        managed = True
        db_table = 'catalog_category'
        verbose_name = 'catalog_category'
        verbose_name_plural = 'catalog_categories'

    def __str__(self):
        return self.title
        # return f"{self.title}, {self.image}, {self.body}, {self.user}"
