# Generated by Django 3.2.10 on 2022-07-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220722_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='img',
            field=models.ImageField(null=True, upload_to='student_img'),
        ),
    ]
