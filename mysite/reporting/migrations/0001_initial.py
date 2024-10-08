# Generated by Django 5.0 on 2024-10-03 04:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.county')),
            ],
        ),
        migrations.CreateModel(
            name='PollingStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.constituency')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_type', models.CharField(choices=[('voter_intimidation', 'Voter Intimidation'), ('machine_malfunction', 'Voting Machine Malfunction'), ('long_wait_times', 'Long Wait Times'), ('misinformation', 'Misinformation'), ('other', 'Other')], max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('evidence', models.FileField(blank=True, null=True, upload_to='incident_evidence/')),
                ('contact_info', models.CharField(blank=True, max_length=255)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('constituency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.constituency')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.county')),
                ('polling_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.pollingstation')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.CharField(max_length=100)),
                ('votes', models.IntegerField()),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.constituency')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.county')),
                ('polling_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.pollingstation')),
            ],
        ),
    ]
