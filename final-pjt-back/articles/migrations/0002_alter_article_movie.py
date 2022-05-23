# Generated by Django 3.2.12 on 2022-05-22 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220520_1624'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
