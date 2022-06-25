from django.contrib import admin

from .models import Brand, Categories,Product,Album_images

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Album_images)
