# Generated by Django 4.1.2 on 2022-11-11 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_sponsorwallet_spent_amount'),
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='sponsor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_donate', to='sponsor.sponsorwallet'),
        ),
    ]
