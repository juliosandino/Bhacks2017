# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class District(models.Model):
    zip_code = models.IntegerField();
    congressional_district = models.IntegerField();

    def __str__(self):
        return self.zip_code