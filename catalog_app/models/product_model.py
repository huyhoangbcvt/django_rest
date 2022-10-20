from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# from user_app.models.account_model import Profile
from .category_model import Category
from django import forms


# @python_2_unicode_compatible
class Product(models.Model):
    # p_title = models.CharField(max_length=255, null=True, default=None)
    p_name = models.CharField(max_length=100, null=True, default=None)
    p_code = models.CharField(max_length=50, unique=True)
    p_image = models.ImageField(upload_to='products/', null=True, default=None, blank=True)
    p_description = models.TextField(max_length=1000, null=True, default=None, blank=True)
    p_country = models.CharField(max_length=50, null=True, default=None, blank=True)
    created_at = models.DateTimeField(null=True, default=datetime.now, blank=True)
    updated_at = models.DateTimeField(null=True, default=datetime.now, blank=True)  # auto_now_add=True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='catalog_products')
    # category = models.ManyToManyField(Category, help_text='Select a Category for this Product')
    # middles = models.ManyToManyField(Category, through='Middleship')
    active = models.BooleanField(
        _("post status"),
        default=True,
        help_text=_("Open - close status post with user"),
    )

    def __str__(self):
        return self.p_title
        # return f"{self.p_title}, {self.p_name}, {self.p_code}, {self.p_date}, {self.p_country}"

    # def __unicode__(self):
    #     return u"%s" % self.user

    class Meta:
        ordering = ['created_at', 'p_name']
        managed = True
        db_table = 'catalog_product'
        verbose_name = 'catalog_product'
        verbose_name_plural = 'catalog_products'

