from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, YearArchiveView
from django.views.generic.base import View
from django.views.generic.list import ListView

from learn_django.otusPlus.forms import forms, CourseSimpleForm, TeacherSimpleForm, StudentSimpleForm
from learn_django.otusPlus.models import Course, Student, Lesson, Document


class CreateCourseView(View):
    form = forms.CourseSimpleForm

    def get(self, request):
        form = self.form()
        return render(request, 'create_course.html', context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            Course.objects.create(**form.cleaned_data)
        return render(request, 'create_course.html', context={"form": form})


class CreateStudentView(View):

    form = StudentSimpleForm

    def get(self, request):
        form = self.form()
        return render(request, 'create_student.html', context={"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_student.html', context={"form": form})
