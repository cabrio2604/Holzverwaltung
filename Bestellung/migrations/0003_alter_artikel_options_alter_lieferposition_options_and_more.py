# Generated by Django 5.1.3 on 2024-12-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bestellung', '0002_artikel_lagerplatz_lieferposition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lieferposition',
            options={'verbose_name': 'Lieferposition', 'verbose_name_plural': 'Lieferpositionen'},
        ),
        migrations.AlterField(
            model_name='artikel',
            name='bezeichnung',
            field=models.CharField(max_length=250, verbose_name='Bezeichnung'),
        ),
    ]
