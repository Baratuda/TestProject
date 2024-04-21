from django.contrib import admin
from .models import *

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)} 
    ordering = ['title']
    exclude = ['main_menu']
