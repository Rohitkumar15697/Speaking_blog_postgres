# Generated by Django 3.2.5 on 2021-07-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_commentmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
