# Generated by Django 2.2.14 on 2020-08-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otusPlus', '0002_auto_20200802_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='otusPlus.Student'),
        ),
    ]
