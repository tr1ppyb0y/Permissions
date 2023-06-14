# Generated by Django 4.2.1 on 2023-05-21 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeadQuater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.company')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.location')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.plant')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.plant')),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.department')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.plant')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.headquater'),
        ),
    ]