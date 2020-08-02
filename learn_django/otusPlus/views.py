from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Document, Course, Student, Teacher


def index_view(request):
    # return HttpResponse('<h1>Hello, OtusPlus index!</h1>')

    document = Document.objects.get(pk=1)
    context = {
        'foo': 'bar',
        'document': document,
        'all_docs': Document.objects.all(),
        'all_students': Student.objects.all(),
        'all_courses': Course.objects.all(),
        'all_teachers': Teacher.objects.all(),

    }
    return render(request, 'otusPlus/index.html', context=context)
