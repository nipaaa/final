# Generated by Django 3.1.7 on 2021-05-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='licence',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/nid/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='nid',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/nid/'),
        ),
    ]
