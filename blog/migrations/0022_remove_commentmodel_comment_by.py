# Generated by Django 3.2.5 on 2021-07-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210709_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='comment_by',
        ),
    ]