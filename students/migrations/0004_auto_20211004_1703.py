# Generated by Django 3.2.7 on 2021-10-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20211004_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_strength',
            name='class1',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class2',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class3',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class4',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class5',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class6',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class7',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='students_strength',
            name='class8',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]