from django.db import models


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

    @property
    def __str__(self):
        return self.title

    teacher = models.ForeignKey(Teacher, on_delete=PROTECT)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    course = models.ForeignKey(Course, on_delete=models.PROTECT)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    course = models.ForeignKey(Course, on_delete=models.PROTECT)


class Documents(models.Model):

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


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    document = models.ForeignKey(Documents, on_delete=models.PROTECT)


class Lesson(models.Model):
    theme_of_lesson = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_time_of_lesson = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.theme_of_lesson


class Calendar(models.Model):
    date = models.DateField()
    lesson = models.ForeignKey(Lesson, on_delete=PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=PROTECT)

