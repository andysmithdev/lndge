# Generated by Django 3.2.7 on 2022-01-06 10:26

from django.db import migrations, models

def update_cost_to(apps, schedma_editor):
    payments = apps.get_model('gui', 'payments')
    hops = apps.get_model('gui', 'paymenthops')
    for payment in payments.objects.all().iterator():
        cost_to = 0
        for hop in hops.objects.filter(payment_hash=payment.payment_hash).order_by('step'):
            hop.cost_to = round(cost_to, 3)
            hop.save()
            cost_to += hop.fee

class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0015_invoices_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='channels',
            name='num_updates',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymenthops',
            name='cost_to',
            field=models.FloatField(default=0),
        ),
        migrations.RunPython(update_cost_to),
        migrations.AlterField(
            model_name='paymenthops',
            name='cost_to',
            field=models.FloatField(),
        ),
    ]