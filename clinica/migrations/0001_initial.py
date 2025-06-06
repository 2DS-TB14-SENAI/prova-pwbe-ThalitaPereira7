# Generated by Django 4.2 on 2025-04-04 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('especialidade', models.CharField(choices=[('PED', 'Pediatria'), ('GIN', 'Ginecologia '), ('OFT', 'Oftalmologia')], max_length=30)),
                ('crm', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=50)),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('AGE', 'agendado'), ('REAL', 'realizado'), ('CANCEL', 'cancelado')], max_length=30)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
