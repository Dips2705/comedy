# Generated by Django 2.2.4 on 2019-08-12 07:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('tagLine', models.CharField(blank=True, max_length=1000)),
                ('cityOfOrigin', models.CharField(max_length=50)),
                ('youtubeUrl', models.URLField()),
                ('linkedinUrl', models.URLField(blank=True)),
                ('websiteUrl', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCritic', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('comedian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comedian')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('comment', models.CharField(max_length=2000)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
    ]
