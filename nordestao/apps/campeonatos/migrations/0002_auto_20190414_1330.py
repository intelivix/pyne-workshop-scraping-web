# Generated by Django 2.1.7 on 2019-04-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='state',
            field=models.CharField(choices=[('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=20),
        ),
    ]
