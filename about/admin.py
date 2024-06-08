from django.contrib import admin

from about.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'image',)