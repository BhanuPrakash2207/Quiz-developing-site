# Generated by Django 4.1.7 on 2023-06-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=250, null=True)),
                ('op1', models.CharField(max_length=250, null=True)),
                ('op2', models.CharField(max_length=250, null=True)),
                ('op3', models.CharField(max_length=250, null=True)),
                ('op4', models.CharField(max_length=250, null=True)),
                ('ans', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
