# Generated by Django 3.2.7 on 2021-10-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_alter_loan_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loantype', to='loans.loan_template'),
        ),
    ]