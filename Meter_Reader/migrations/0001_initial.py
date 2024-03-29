# Generated by Django 3.2.21 on 2023-10-21 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('consumer_no', models.CharField(max_length=100)),
                ('connection_type', models.CharField(max_length=100)),
                ('AREA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.area')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('BRANCH', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.branch')),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.login')),
            ],
        ),
        migrations.CreateModel(
            name='unit_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_type', models.CharField(max_length=100)),
                ('unit_from', models.CharField(max_length=100)),
                ('unit_to', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('last_updated', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='work_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AREA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.area')),
                ('STAFF', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.staff')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('CONSUMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('BRANCH', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.branch')),
            ],
        ),
        migrations.AddField(
            model_name='consumer',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.login'),
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('complaint_date', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('reply_date', models.CharField(max_length=100)),
                ('CONSUMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.consumer')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.login'),
        ),
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('current_reading', models.CharField(max_length=100)),
                ('unit_consumed', models.CharField(max_length=100)),
                ('status', models.CharField(default=1, max_length=100)),
                ('CONSUMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.consumer')),
            ],
        ),
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('account_no', models.CharField(max_length=100)),
                ('IFSC_code', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.login')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='BRANCH',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Meter_Reader.branch'),
        ),
    ]
