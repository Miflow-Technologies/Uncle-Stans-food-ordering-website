# Generated by Django 4.1.7 on 2023-06-04 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('packs', 'PACKS'), ('platter for 5', 'PLATTER5'), ('platter for 10', 'PLATTER10'), ('extras', 'EXTRAS')], max_length=100),
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='main.category'),
        ),
    ]
