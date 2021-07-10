# Generated by Django 3.2.5 on 2021-07-10 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0030_commentmodel_comment_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='comment_by',
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
