# Generated by Django 4.0.3 on 2022-04-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, default='house.jpg', null=True, upload_to='houses_pics'),
        ),
    ]
