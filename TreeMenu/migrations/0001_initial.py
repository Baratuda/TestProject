# Generated by Django 4.2.3 on 2024-04-18 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('main_menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='TreeMenu.menu')),
                ('parent', models.ForeignKey(blank=True, default='None', on_delete=django.db.models.deletion.CASCADE, related_name='children', to='TreeMenu.menu')),
            ],
            options={
                'verbose_name': 'меню',
                'verbose_name_plural': 'Список меню',
                'unique_together': {('title', 'parent')},
            },
        ),
    ]
