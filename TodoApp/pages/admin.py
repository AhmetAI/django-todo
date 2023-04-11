from django.contrib import admin
from pages.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "slug","author")
    list_display_links = ("title", "slug",)
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("title","date","author")
    search_fields = ("title","description")

