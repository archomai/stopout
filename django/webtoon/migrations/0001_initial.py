# Generated by Django 2.0.2 on 2018-02-03 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=100)),
                ('created_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webtoon_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='webtoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtoon.Webtoon'),
        ),
    ]
