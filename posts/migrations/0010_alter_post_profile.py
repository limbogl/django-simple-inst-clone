# Generated by Django 3.2.2 on 2021-07-30 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_date_created'),
        ('posts', '0009_alter_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
