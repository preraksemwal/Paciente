# Generated by Django 4.1.3 on 2022-11-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_doctor_healthcare_professional'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=122)),
                ('patient_email', models.EmailField(max_length=122)),
                ('doctor_email', models.EmailField(max_length=122)),
                ('description', models.CharField(max_length=122)),
                ('date', models.DateField(max_length=122)),
                ('time', models.TimeField(max_length=122)),
            ],
        ),
    ]
