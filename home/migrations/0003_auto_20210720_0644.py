# Generated by Django 3.2.5 on 2021-07-20 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_about_us_setting_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='brand_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='setting',
            name='shopping_features_description',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='shopping_features_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='setting',
            name='shopping_features_title',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
