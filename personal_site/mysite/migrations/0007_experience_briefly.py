# Generated by Django 4.1.7 on 2023-07-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_education_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='briefly',
            field=models.TextField(default=1, help_text='Введите свой опыт', max_length=5000, verbose_name='Опыт работы'),
            preserve_default=False,
        ),
    ]
