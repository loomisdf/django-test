from django.contrib import admin
from polls.models import Question

# Register your models here.
class QuestionAdmin(admin.MOdelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
