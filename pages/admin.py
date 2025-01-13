from django.contrib import admin

# from .models import HomePage
from .models import HomePage


class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["site_name", "site_tagline"]}),
    ]
    list_display = ["site_name", "site_tagline"]
    search_fields = ["site_name"]


# Register your models here.
admin.site.register(HomePage, HomePageAdmin)
