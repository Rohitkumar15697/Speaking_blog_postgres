# Generated by Django 3.2.5 on 2021-08-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20210801_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
