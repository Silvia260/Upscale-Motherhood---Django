# Generated by Django 2.2 on 2022-03-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pro_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nanny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('location', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=60)),
                ('rate', models.IntegerField(blank=True, default=400)),
                ('phonenumber', models.IntegerField()),
                ('featured', models.BooleanField()),
                ('bio', models.CharField(max_length=200)),
                ('pro_skills', models.ManyToManyField(to='motherhood.pro_skills')),
            ],
        ),
    ]