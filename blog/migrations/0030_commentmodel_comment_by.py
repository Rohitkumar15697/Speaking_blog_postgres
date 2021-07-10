# Generated by Django 3.2.5 on 2021-07-10 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0029_alter_commentmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='comment_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
