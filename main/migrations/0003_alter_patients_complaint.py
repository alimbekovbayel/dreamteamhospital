# Generated by Django 4.1.6 on 2023-02-06 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_hospital_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='complaint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.chief_physician', verbose_name='Жалоба'),
        ),
    ]
