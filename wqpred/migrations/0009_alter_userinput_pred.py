# Generated by Django 4.2.3 on 2023-07-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqpred', '0008_userinput_pred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='pred',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
