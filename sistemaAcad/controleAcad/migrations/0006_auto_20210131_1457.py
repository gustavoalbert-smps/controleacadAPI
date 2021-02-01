# Generated by Django 3.1.5 on 2021-01-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleAcad', '0005_auto_20210129_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='bimestre',
            field=models.IntegerField(choices=[(1, '1º BIMESTRE'), (2, '2º BIMESTRE')]),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.IntegerField(choices=[(0, '0.0'), (0.5, '0.5'), (1, '1.0'), (1.5, '1.5'), (2, '2.0'), (2.5, '2.5'), (3, '3.0'), (3.5, '3.5'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'), (7, '7.0'), (7.5, '7.5'), (8, '8.0'), (8.5, '8.5'), (9, '9.0'), (9.5, '9.5'), (10, '10.0')]),
        ),
        migrations.AlterField(
            model_name='nota',
            name='periodo',
            field=models.IntegerField(choices=[(1, '1º PERÍODO'), (2, '2º PERÍODO'), (3, '3º PERÍODO'), (4, '4º PERÍODO'), (5, '5º PERÍODO'), (6, '6º PERÍODO')], default=1),
        ),
    ]
