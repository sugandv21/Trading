from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import SiteAsset  

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


@admin.register(SiteAsset)
class SiteAssetAdmin(admin.ModelAdmin):
    list_display = ("key", "image")
    search_fields = ("key",)
