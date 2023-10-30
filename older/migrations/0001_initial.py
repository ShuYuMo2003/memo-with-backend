# Generated by Django 4.2.3 on 2023-10-30 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('photos_uuid', models.JSONField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('TW', 'Transgender Woman'), ('TM', 'Transgender Man')], max_length=5, null=True)),
                ('lost_place', models.TextField(blank=True, null=True)),
                ('lost_date', models.DateTimeField(blank=True, null=True)),
                ('family_name', models.TextField()),
                ('family_phone', models.TextField()),
                ('family_email', models.TextField(blank=True, null=True)),
                ('family_address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
