# Generated by Django 2.1.5 on 2020-12-14 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201213_2220'),
        ('app', '0003_menuitem_is_healthy'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='user_order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile'),
        ),
    ]