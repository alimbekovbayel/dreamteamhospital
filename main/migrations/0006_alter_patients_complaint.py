# Generated by Django 4.1.6 on 2023-02-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_patients_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='complaint',
            field=models.CharField(max_length=1000, null=True, verbose_name='Жалоба'),
        ),
    ]
