# Generated by Django 3.2.10 on 2022-08-10 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_health_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='choise2',
            field=models.ImageField(null=True, upload_to='vax_cards'),
        ),
        migrations.AlterField(
            model_name='health',
            name='phonenumber',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='temperature',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
