# Generated by Django 2.1.5 on 2020-12-16 20:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201213_2220'),
        ('app', '0004_menuitem_user_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_of_people', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('telephone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "+999999999".Up to 15 digits allowed.', regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254)),
                ('order_profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile')),
                ('order_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Restaurant')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='user_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Order'),
        ),
    ]
