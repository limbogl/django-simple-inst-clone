# Generated by Django 3.2.2 on 2021-08-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]