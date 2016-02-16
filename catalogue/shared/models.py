# -*- coding: utf-8 -*-
from django.db import models

class BaseModel(models.Model):
    """
    All models defined in my apps should be based on this abstract model. It adds
    datetime fields for creation and editing of each model instance.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
