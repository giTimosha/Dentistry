# Generated by Django 2.2.1 on 2020-01-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentistry', '0002_auto_20200113_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='employee_lastName',
            field=models.CharField(max_length=30, verbose_name='Фамилия сотрудника'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
