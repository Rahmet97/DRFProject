# Generated by Django 4.1.1 on 2022-09-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=4),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=4),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='view',
            field=models.CharField(choices=[('Flat', 'Flat'), ('House', 'House'), ('Office', 'Office')], max_length=6),
        ),
    ]