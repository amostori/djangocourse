# Generated by Django 5.1.4 on 2025-01-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_userprofile_managers_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('inprogress', 'In Progress'), ('published', 'Published')], default='draft', max_length=20),
        ),
    ]