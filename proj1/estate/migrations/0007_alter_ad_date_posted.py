# Generated by Django 4.0.3 on 2022-04-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]