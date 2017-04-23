# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from candidates.models import District, CongressMan
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["__str__", "congressional_district"]

class CongressManAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "district", "party"]

admin.site.register(District, DistrictAdmin)
admin.site.register(CongressMan, CongressManAdmin)
