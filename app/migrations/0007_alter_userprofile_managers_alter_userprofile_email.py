# Generated by Django 5.1.4 on 2025-01-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]