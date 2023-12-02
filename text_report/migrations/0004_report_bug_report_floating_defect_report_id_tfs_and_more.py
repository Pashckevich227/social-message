# Generated by Django 4.2.7 on 2023-12-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_report', '0003_report_url_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='bug',
            field=models.CharField(choices=[('1', 'Дефект продукта'), ('2', 'Дефект автостенда'), ('3', 'Новый дефект'), ('4', 'Доработка автотеста'), ('5', 'Возможный дефект продукта')], default=1, max_length=30),
        ),
        migrations.AddField(
            model_name='report',
            name='floating_defect',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='id_tfs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='my_solution',
            field=models.TextField(null=True),
        ),
    ]
