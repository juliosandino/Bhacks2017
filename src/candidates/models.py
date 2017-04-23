# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class District(models.Model):
    zip_code = models.IntegerField()
    congressional_district = models.IntegerField()

    def __str__(self):
        return self.zip_code

class CongressMan(models.Model):
    name = models.CharField(max_length=140)
    stance = models.CharField(max_length=1)
    party = models.CharField(max_length=15)
    incumbent = models.CharField(max_length=3)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)

    def __str__(self):
        return name

