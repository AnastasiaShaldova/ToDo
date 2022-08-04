# Generated by Django 4.1 on 2022-08-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_alter_users_first_name_alter_users_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
