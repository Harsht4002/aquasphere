# Generated by Django 4.2.16 on 2024-11-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_campaign_options_alter_subscriber_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='campaign',
        ),
        migrations.DeleteModel(
            name='Campaign',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]