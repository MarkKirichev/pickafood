# Generated by Django 2.1.5 on 2020-12-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201216_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_order',
            field=models.TextField(),
        ),
    ]
