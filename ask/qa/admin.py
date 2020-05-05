from django.contrib import admin

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]


admin.site.register(Question, QuestionAdmin)
