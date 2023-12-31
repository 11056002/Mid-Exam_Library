# Generated by Django 4.2.6 on 2023-10-27 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=4)),
                ('age', models.IntegerField(default=0)),
                ('tel', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LmsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('addr', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('img_and_con', models.TextField()),
                ('ISBN', models.CharField(max_length=64)),
                ('translator', models.CharField(max_length=64)),
                ('date', models.DateField(blank=True)),
                ('status', models.CharField(max_length=10)),
                ('author', models.ManyToManyField(to='mysite.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.publisher')),
            ],
        ),
    ]
