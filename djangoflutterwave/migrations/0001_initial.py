# Generated by Django 3.1.4 on 2020-12-18 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlwPlanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('flw_plan_id', models.PositiveIntegerField(blank=True, help_text='Flutterwave plan id. Only required if this is a subscription plan.', null=True, unique=True)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('modal_logo_url', models.URLField(blank=True, help_text='URL to logo image to be displayed on payment modal.', max_length=500, null=True)),
                ('modal_title', models.CharField(blank=True, help_text='Title to be displayed on payment modal.', max_length=200, null=True)),
                ('pay_button_text', models.CharField(default='Sign Up', help_text='Text used for button when displayed in a template.', max_length=100)),
                ('pay_button_css_classes', models.CharField(blank=True, help_text='css classes to be applied to pay button in template.', max_length=200, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='FlwTransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('tx_ref', models.CharField(max_length=100)),
                ('flw_ref', models.CharField(max_length=100)),
                ('device_fingerprint', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(max_length=3)),
                ('charged_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('app_fee', models.DecimalField(decimal_places=2, max_digits=9)),
                ('merchant_fee', models.DecimalField(decimal_places=2, max_digits=9)),
                ('processor_response', models.CharField(max_length=100)),
                ('auth_model', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('narration', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('payment_type', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=100)),
                ('account_id', models.PositiveIntegerField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flw_transactions', to='djangoflutterwave.flwplanmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flw_transactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
