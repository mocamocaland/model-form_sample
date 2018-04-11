from django.contrib import admin
from .models import Day, Category

class DayInline(admin.StackedInline):
    model = Day
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    inlines = [DayInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Day)
