from django.contrib import admin
from app.models import Article, UserProfile
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'word_count', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    readonly_fields = ('word_count', 'created_at', 'updated_at')


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permission")}),
        ("Important dates", {"fields": ("last_login", "date_joined")})
    )
    add_fieldsets = (
        (None, {"classes": ("wide",),
                "fields": ("email", "password1", "password2")}),
    )
    list_display = ( "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_field = ("email",)
    ordering = ("email",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)
