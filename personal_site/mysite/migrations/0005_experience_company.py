# Generated by Django 4.1.7 on 2023-07-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_desirerole'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]