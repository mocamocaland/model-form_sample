# Generated by Django 2.0.3 on 2018-04-11 05:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='タイトル')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='カテゴリ', to='form.Category')),
            ],
        ),
    ]
