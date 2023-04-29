from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner
from .models import Question, Choice


# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #list_display = ['question_text']
    inlines = [ChoiceInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]


# <HINT> Register Question and Choice models here
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
