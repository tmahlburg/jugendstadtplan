# Generated by Django 3.1.2 on 2020-10-29 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_proposal', models.TextField(verbose_name='Was sollte hier anders sein?')),
                ('location_to_change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.location', verbose_name='ID des zu ändernden Ortes')),
            ],
        ),
    ]
