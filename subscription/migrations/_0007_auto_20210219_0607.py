# Generated by Django 3.0.7 on 2021-02-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20210219_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_af',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ast',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_az',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_be',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_bg',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_bn',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_br',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_bs',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ca',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_cs',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_cy',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_da',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_de',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_dsb',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_el',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en_au',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en_gb',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_eo',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es_co',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es_mx',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es_ni',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es_ve',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_et',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_eu',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fi',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fr',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_fy',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ga',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_gd',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_gl',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_he',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hi',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hr',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hsb',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hu',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hy',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ia',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_id',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_io',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_is',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_it',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ja',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ka',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_kab',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_kk',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_km',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_kn',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ko',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_lb',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_lt',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_lv',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_mk',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ml',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_mn',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_mr',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_my',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_nb',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ne',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_nl',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_nn',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_os',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_pa',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_pl',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_pt',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_pt_br',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ro',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sk',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sl',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sq',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sr',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sr_latn',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sv',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_sw',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ta',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_te',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_th',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_tt',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_udm',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ur',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_vi',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_zh_hans',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_zh_hant',
            field=models.CharField(max_length=200, null=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_af',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ast',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_az',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_be',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bg',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bn',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_br',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bs',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ca',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_cs',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_cy',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_da',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_de',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_dsb',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_el',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en_au',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en_gb',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_eo',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es_co',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es_mx',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es_ni',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es_ve',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_et',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_eu',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fi',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fr',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_fy',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ga',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_gd',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_gl',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_he',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hi',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hr',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hsb',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hu',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hy',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ia',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_id',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_io',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_is',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_it',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ja',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ka',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_kab',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_kk',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_km',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_kn',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ko',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_lb',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_lt',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_lv',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_mk',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ml',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_mn',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_mr',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_my',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_nb',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ne',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_nl',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_nn',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_os',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_pa',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_pl',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_pt',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_pt_br',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ro',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sk',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sl',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sq',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sr',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sr_latn',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sv',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_sw',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ta',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_te',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_th',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_tr',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_tt',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_udm',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ur',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_vi',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_zh_hans',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_zh_hant',
            field=models.CharField(max_length=200, null=True, verbose_name='question'),
        ),
    ]
