# Generated by Django 3.0.5 on 2020-05-02 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='of',
            new_name='user',
        ),
    ]
