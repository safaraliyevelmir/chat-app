# Generated by Django 4.0.5 on 2022-07-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(default='static/images/pp.jpeg', upload_to='profile_photo/'),
        ),
    ]
