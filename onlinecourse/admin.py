from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission
)


# Inline for Lesson inside Course
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Inline for Choice inside Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Course admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Lesson admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']


# Register models (ONLY ONCE)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
