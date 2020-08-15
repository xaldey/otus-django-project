from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from learn_django.otusPlus.models import Author, Document, Course, Student, Teacher, Lesson


def index_view(request):
    # return HttpResponse('<h1>Hello, OtusPlus index!</h1>')
    right_now = datetime.now()
    document = Document.objects.get(pk=1)
    context = {
        'foo': 'bar',
        'document': document,
        'all_docs': Document.objects.all(),
        'all_students': Student.objects.all(),
        'all_courses': Course.objects.all(),
        'all_teachers': Teacher.objects.all(),
        'all_lessons': Lesson.objects.all(),
        'hot_lessons': Lesson.objects.all()

    }
    return render(request, 'index.html', context=context)
