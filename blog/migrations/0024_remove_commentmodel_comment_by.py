# Generated by Django 3.2.5 on 2021-07-10 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_commentmodel_comment_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='comment_by',
        ),
    ]
