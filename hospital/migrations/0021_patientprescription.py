# Generated by Django 3.1.7 on 2021-06-20 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_doctor_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40)),
                ('assignedDoctorName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('releaseDate', models.DateField()),
                ('medicine', models.TextField(max_length=500, null=True)),
                ('test', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
