from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Transaction)