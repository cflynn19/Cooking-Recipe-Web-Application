# Generated by Django 3.2.16 on 2022-10-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientsSearch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='text',
        ),
        migrations.AlterField(
            model_name='search',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]