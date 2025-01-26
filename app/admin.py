from django.contrib import admin
from app.models import UserProfile, Article
from django.contrib.auth.admin import UserAdmin


# aby sprecyzowac co i jak ma byc wyswietlane w panelu admina stworz klase
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', )
    search_fields = ('title', 'content', )
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    readonly_fields = ('word_count','created_at') 


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # pola, gdy tworzy sie nowy uzytkownik
    add_fieldsets = (
        # None to title dla pola
        (None, {
            'classes': ('wide',), # chodzi o klasy CSS
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
