# Generated by Django 4.2.3 on 2024-04-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TreeMenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='main_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TreeMenu.menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='TreeMenu.menu'),
        ),
    ]