# Generated by Django 3.2.5 on 2021-07-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210705_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
