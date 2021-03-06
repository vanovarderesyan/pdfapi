# Generated by Django 3.0.7 on 2021-02-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20210219_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_en_us', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_en_gb', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_fi', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_pt', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_pt_br', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_fr', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('question_es', models.CharField(max_length=200, null=True, verbose_name='question')),
                ('answer_en_us', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_en_gb', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_fi', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_pt', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_pt_br', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_fr', models.CharField(max_length=200, null=True, verbose_name='answer')),
                ('answer_es', models.CharField(max_length=200, null=True, verbose_name='answer')),
            ],
        ),
    ]
