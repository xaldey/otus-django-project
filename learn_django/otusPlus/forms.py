from django import forms
from .models import Author, Course, Teacher, Document, Student, Lesson, Calendar


class CourseSimpleForm(forms.Form):
    title = forms.CharField()
    what_to_learn = forms.ChoiceField(queryset=Course.objects.all(), label="WHAT_TO_LEARN")
    teacher = forms.ChoiceField(queryset=Teacher.objects.all(),label="Teacher")


class TeacherSimpleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


class StudentSimpleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    course = forms.ChoiceField(queryset=Course.objects.all(), label="Course")