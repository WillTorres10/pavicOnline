# Generated by Django 2.0.5 on 2018-06-08 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0009_biblioteca_pdf_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblioteca',
            name='PDF_Arquivo',
        ),
    ]
