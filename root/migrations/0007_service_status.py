# Generated by Django 4.2 on 2024-08-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_alter_service_content1_alter_service_content2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
