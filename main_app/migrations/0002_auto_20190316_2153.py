# Generated by Django 2.1.7 on 2019-03-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='food_allergy',
            field=models.CharField(choices=[('M', 'Milk'), ('E', 'Eggs'), ('P', 'Peanuts')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='parent',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]