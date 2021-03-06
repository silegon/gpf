# Generated by Django 2.2 on 2019-04-17 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=64, null=True)),
                ('avatar', models.URLField(blank=True, default='', max_length=255)),
                ('uid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('desc', models.CharField(blank=True, default='', max_length=255)),
                ('main_language', models.CharField(max_length=32)),
                ('star_count', models.IntegerField(default=0)),
                ('issues_count', models.IntegerField(default=0)),
                ('update', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.IntegerField(choices=[(0, 'CreateEvent'), (1, 'WatchEvent'), (2, 'ForkEvent'), (3, 'PublicEvent')])),
                ('event_id', models.IntegerField(blank=True, null=True)),
                ('create', models.DateTimeField(blank=True, null=True)),
                ('repository', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.Repository')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.GithubUser')),
            ],
        ),
    ]
