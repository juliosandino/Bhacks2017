# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from candidates.models import District
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["__str__", "congressional_district"]

admin.site.register(District, DistrictAdmin)
