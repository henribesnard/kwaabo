from django.contrib import admin

from .models import parametre_recherche, buckets, items, legs, segments

admin.site.register(parametre_recherche)
admin.site.register(buckets)
admin.site.register(items)
admin.site.register(legs)
admin.site.register(segments)
