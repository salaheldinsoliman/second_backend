# Generated by Django 3.2.7 on 2021-10-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_alter_loan_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='type',
            field=models.CharField(max_length=1),
        ),
    ]
