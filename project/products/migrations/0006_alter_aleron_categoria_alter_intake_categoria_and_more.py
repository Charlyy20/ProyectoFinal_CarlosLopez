# Generated by Django 5.0.4 on 2024-05-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_aleron_intake_llanta_spoiler_delete_alerones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aleron',
            name='categoria',
            field=models.CharField(choices=[('llanta', 'Llanta'), ('aleron', 'Aleron'), ('spoiler', 'Spoiler'), ('intake', 'Intake'), ('widebody', 'Widebody')], default='llanta', max_length=30),
        ),
        migrations.AlterField(
            model_name='intake',
            name='categoria',
            field=models.CharField(choices=[('llanta', 'Llanta'), ('aleron', 'Aleron'), ('spoiler', 'Spoiler'), ('intake', 'Intake'), ('widebody', 'Widebody')], default='llanta', max_length=30),
        ),
        migrations.AlterField(
            model_name='llanta',
            name='categoria',
            field=models.CharField(choices=[('llanta', 'Llanta'), ('aleron', 'Aleron'), ('spoiler', 'Spoiler'), ('intake', 'Intake'), ('widebody', 'Widebody')], default='llanta', max_length=30),
        ),
        migrations.AlterField(
            model_name='spoiler',
            name='categoria',
            field=models.CharField(choices=[('llanta', 'Llanta'), ('aleron', 'Aleron'), ('spoiler', 'Spoiler'), ('intake', 'Intake'), ('widebody', 'Widebody')], default='llanta', max_length=30),
        ),
        migrations.AlterField(
            model_name='widebody',
            name='categoria',
            field=models.CharField(choices=[('llanta', 'Llanta'), ('aleron', 'Aleron'), ('spoiler', 'Spoiler'), ('intake', 'Intake'), ('widebody', 'Widebody')], default='llanta', max_length=30),
        ),
    ]
