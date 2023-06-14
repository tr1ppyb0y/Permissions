from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    # id is auto generated.
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'
    
    def __siblings(self, cls_obj):
        siblings = {}
        for f in cls_obj._meta.local_fields:
            if isinstance(f, models.ForeignKey) and f.related_model:
                siblings = {m:m.related_model for m in f.related_model._meta.related_objects}
        return siblings

    def __child_level_stack(self, cls_obj):
        m2o = {m:m.related_model for m in cls_obj._meta.related_objects}
        siblings = self.__siblings(cls_obj)
        children = set(m2o.values())
        if siblings:
            children -= set(siblings.values())            
        return [(k, v) for k, v in m2o.items() if v in children]

    def __compute_permissions(self):
        stack = self.__child_level_stack(self.content_object)
        permissions = set()
        while stack:
            m2o, cls_obj = stack.pop()
            stack.extend(self.__child_level_stack(cls_obj))
            con = ContentType.objects.get_for_model(m2o.field.model)
            permissions |= set(con.levelpermission_set.values_list('tag', flat=True))
        return permissions

    def my_permissions(self):
        permissions = set(self.content_type.levelpermission_set.values_list('tag', flat=True))
        permissions |= self.__compute_permissions()
        return permissions

class LevelPermission(models.Model):
    # id is auto generated.
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return self.tag
