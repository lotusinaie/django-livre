# Generated by Django 3.2.9 on 2021-12-03 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=10012, unique=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='cpf_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_receiver', to='bank.clients', to_field='cpf', verbose_name='Receiver'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='cpf_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfer_sender', to='bank.clients', to_field='cpf', verbose_name='Sender'),
        ),
    ]
