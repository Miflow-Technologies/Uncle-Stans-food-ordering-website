# Generated by Django 4.2.1 on 2023-06-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_menuitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ManyToManyField(related_name='item', to='main.category'),
        ),
    ]
