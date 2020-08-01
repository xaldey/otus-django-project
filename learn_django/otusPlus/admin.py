from django.contrib import admin

from .models import Author, Document, Student, Teacher, Course, Lesson, Calendar


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "full_name", "last_name"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    def text_short(self, obj:Document):
        if len(obj.text) > 42:
            return f"{obj.text[:42]}..."
        return obj.text
    list_display = "id", "title", "text_short", "type_of_doc", "time_to_read", "ts_created", \
                   "ts_last_changed",  "author"
    list_display_links = "title", "text_short"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "full_name", "last_name"


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_name", "full_name"
    list_display_links = "full_name", "last_name"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "id", "title", "what_to_learn"
