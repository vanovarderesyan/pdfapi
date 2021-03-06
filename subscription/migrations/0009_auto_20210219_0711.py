# Generated by Django 3.0.7 on 2021-02-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0008_auto_20210219_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='is_free',
        ),
        migrations.AddField(
            model_name='subscription',
            name='type',
            field=models.IntegerField(blank=True, choices=[('0', 'FREE'), ('1', 'CHEAP'), ('2', 'EXPENSIVE')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.FloatField(),
        ),
    ]
