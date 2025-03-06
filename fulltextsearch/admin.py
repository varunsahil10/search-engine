from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pid','name','brand','gender','price','description','color',)

    search_fields = ('pid','name','brand','gender','price','description','color',)

    list_filter = ('brand','gender','color',)

    readonly_fields = ('name','description')
    exclude = ('pid',)

    actions = ['mark_color_peach']

    def mark_color_peach(self,request,queryset):
        queryset.update(
            color = 'Peach'
        )
