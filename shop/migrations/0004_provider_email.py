# Generated by Django 2.1.2 on 2018-10-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181005_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='email',
            field=models.EmailField(default='JakNowySolutions@gmail.com', max_length=50),
        ),
    ]