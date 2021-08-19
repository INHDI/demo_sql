from django.contrib import admin
from .models import *
# Register your models here.
class LoginModelAdmin(admin.ModelAdmin):
    list_display = ('user','pas',)

class ThemSuaXoaAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    search_fields = ['title']
admin.site.register(LoginModel, LoginModelAdmin)
admin.site.register(ThemSuaXoa, ThemSuaXoaAdmin)