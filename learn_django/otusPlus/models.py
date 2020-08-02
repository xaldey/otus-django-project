from django.db import models
from django.db.models import PROTECT, SET_NULL


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Document(models.Model):

    TYPE_OF_DOC = (
        (1, 'article'),
        (2, 'book'),
        (3, 'scan'),
        (4, 'plan'),
        (5, 'scratch'),
    )

    TIME_TO_READ = (
        (1, '< 1 min'),
        (2, '1 - 5 min'),
        (3, '5 - 10 min'),
        (4, '10 - 15 min'),
        (5, '> 15 min'),
    )

    title = models.CharField(max_length=254)
    text = models.TextField()
    type_of_doc = models.IntegerField(choices=TYPE_OF_DOC)
    time_to_read = models.IntegerField(choices=TIME_TO_READ)
    ts_last_changed = models.DateTimeField(auto_now=True)
    ts_created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    courses = models.ManyToManyField('Course')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Course(models.Model):

    WHAT_TO_LEARN = (
        (1, 'CSS'),
        (2, 'HTML'),
        (3, 'JavaScript'),
        (4, 'Python'),
        (5, 'C++'),
    )

    title = models.CharField(max_length=100)
    what_to_learn = models.IntegerField(choices=WHAT_TO_LEARN)
    teacher = models.ForeignKey(Teacher, on_delete=SET_NULL, null=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    theme_of_lesson = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_time_of_lesson = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.theme_of_lesson


class Calendar(models.Model):
    date = models.DateField()
    time = models.TimeField()



