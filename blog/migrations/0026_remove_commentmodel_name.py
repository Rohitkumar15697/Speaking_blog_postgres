# Generated by Django 3.2.5 on 2021-07-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_commentmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='name',
        ),
    ]
