# Generated by Django 5.1.3 on 2024-12-10 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bestellung', '0003_alter_artikel_options_alter_lieferposition_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'verbose_name': 'Artikel', 'verbose_name_plural': 'Artikel'},
        ),
    ]
