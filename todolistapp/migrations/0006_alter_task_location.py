# Generated by Django 3.2.3 on 2021-05-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0005_alter_task_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.CharField(choices=[('LO', 'London'), ('AL', 'Alaska'), ('NE', 'New York'), ('MO', 'Moscow'), ('TO', 'Tokyo'), ('SH', 'Shanghai'), ('DE', 'Delhi')], default='LO', max_length=3),
        ),
    ]
