from django.db import models
from django.contrib.auth.models import User
# from .product_model import Product
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver

from django.core.exceptions import ImproperlyConfigured
from django.db import models, transaction, router
from django.db.models.signals import post_save, pre_save


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
        managed = True
        ordering = ['created_at', 'title']
        db_table = 'catalog_category'
        verbose_name = 'catalog_category'
        verbose_name_plural = 'catalog_categories'

    def __str__(self):
        return self.title
        # return f"{self.title}, {self.image}, {self.body}, {self.user}"


# Run update_middle() after the end of the save() method
# update_middle
# post_save: Gửi signal khi kết thúc hàm save()
# sender=Category: chỉ nhận signal từ Middle Model
# instance: instance được lưu
# @receiver(post_save, sender=Category)
# # @on_transaction_commit
# def update_middle(sender, instance, created, **kwargs):
#     # If the Category is created successfully
#     if created:
#         # Create user middle
#         Middle.objects.create(user=instance)
#     instance.diddle.save()
#     transaction.on_commit(update_middle)


class SaveSignalHandlingModel(models.Model):
    class Meta:
        abstract = True

    def save(self, signals_to_disable=None, *args, **kwargs):
        self.signals_to_disable = signals_to_disable or []
        super().save(*args, **kwargs)

    def save_base(self, raw=False, force_insert=False, force_update=False, using=None, update_fields=None):
        using = using or router.db_for_write(self.__class__, instance=self)
        assert not (force_insert and (force_update or update_fields))
        assert update_fields is None or len(update_fields) > 0
        cls = origin =   self.__class__

        if cls._meta.proxy:
            cls = cls._meta.concrete_model
        meta = cls._meta
        if not meta.auto_created and 'pre_save' not in self.signals_to_disable:
            pre_save.send(
                sender=origin, instance=self, raw=raw, using=using,
                update_fields=update_fields,
            )
        with transaction.atomic(using=using, savepoint=False):
            if not raw:
                self._save_parents(cls, using, update_fields)
            updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)

        self._state.db = using
        self._state.adding = False

        if not meta.auto_created and 'post_save' not in self.signals_to_disable:
            post_save.send(sender=origin, instance=self, created=(not updated), update_fields=update_fields, raw=raw, using=using)
