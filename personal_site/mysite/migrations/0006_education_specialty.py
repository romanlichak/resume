# Generated by Django 4.1.7 on 2023-07-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_experience_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='specialty',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]