# Generated by Django 4.0.4 on 2022-05-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_slot_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '09:00 am To 10:00 am'), (1, '10:00 Am TO 11:00 Am'), (2, '11:00 Am To 12:00 Am'), (3, '12:00 Am To 01:00 Pm'), (4, '02:00 Pm To 03:00 Pm'), (5, '03:00 Pm To 04:00 Pm'), (6, '04:00 Pm To 05:00 Pm')]),
        ),
    ]
