from django.contrib import admin

from places.models import Country, Town, Library

admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Library)
