# Generated by Django 3.0.7 on 2021-02-19 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_auto_20210218_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiontext',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_text', to='subscription.Subscription'),
        ),
    ]
