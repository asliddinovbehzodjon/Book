# Generated by Django 4.0.4 on 2022-04-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitoblar',
            name='janr',
            field=models.CharField(choices=[('I', 'Ilmiy'), ('B', 'Badiiy '), ('F', 'Fantastik'), ('TB', 'Tarixiy-adabiy'), ('T', 'Tarixiy'), ('D', 'Detektiv'), ('A', 'Avtobiografik'), ('Boshqa', 'Boshqa')], default='Boshqa', max_length=400),
        ),
    ]
