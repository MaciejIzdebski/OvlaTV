# Generated by Django 4.0.5 on 2022-06-09 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_address_person_telephones_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Telephones',
            new_name='Telephone',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
    ]