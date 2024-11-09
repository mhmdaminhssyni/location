from django.contrib import admin
from .models import Document
from django.contrib.admin import register

@register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'upload']
    list_display_links = ['title']