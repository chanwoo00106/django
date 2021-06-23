from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'date')
    search_fields = ['text']

admin.site.register(Question, QuestionAdmin)