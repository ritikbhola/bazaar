# Generated by Django 3.2.3 on 2021-05-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210529_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('L', 'Loafer'), ('SL', 'Sleepers'), ('S', 'Sandel'), ('SP', 'Sports'), ('F', 'Formal Shoes'), ('FSL', 'FSleepers'), ('FS', 'FSandel'), ('T', 'Trending')], max_length=3),
        ),
    ]
