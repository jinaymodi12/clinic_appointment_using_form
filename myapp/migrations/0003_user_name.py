# Generated by Django 4.0.4 on 2022-05-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=98),
            preserve_default=False,
        ),
    ]
