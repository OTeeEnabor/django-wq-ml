# Generated by Django 4.2.3 on 2023-07-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wqpred', '0004_alter_userinput_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
