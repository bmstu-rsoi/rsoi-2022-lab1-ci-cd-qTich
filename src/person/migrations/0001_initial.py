# Generated by Django 4.1.1 on 2022-09-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('work', models.CharField(max_length=255)),
            ],
        ),
    ]
