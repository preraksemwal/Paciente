# Generated by Django 4.1.3 on 2022-11-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_userinfo_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=122)),
                ('lastName', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('loginPassword', models.CharField(max_length=122)),
                ('document', models.FileField(null=True, upload_to='None')),
                ('uploaded_image1', models.FileField(null=True, upload_to='None')),
                ('uploaded_image2', models.FileField(null=True, upload_to='None')),
            ],
        ),
    ]
