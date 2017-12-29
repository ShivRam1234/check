from django.contrib import admin

# Register your models here.
from filmitouch.models import Categories, Language1, Subcategories, Blog, ContactForm1, Advertisement1, Newsletter

admin.site.register(Categories)
admin.site.register(Language1)
admin.site.register(Subcategories)
admin.site.register(Blog)
admin.site.register(ContactForm1)
admin.site.register(Advertisement1)
admin.site.register(Newsletter)