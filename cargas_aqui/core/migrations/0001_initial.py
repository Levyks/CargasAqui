# Generated by Django 4.0.4 on 2022-05-05 13:08

import cargas_aqui.core.managers
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Cargo Status',
                'verbose_name_plural': 'Cargo Statuses',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('abbreviation', models.CharField(max_length=2, verbose_name='Abbreviation')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=255, verbose_name='Route')),
                ('numberOfDeliveries', models.IntegerField(verbose_name='Number of deliveries')),
                ('weightInKg', models.IntegerField(verbose_name='Weight in Kg')),
                ('payment', models.FloatField(verbose_name='Payment')),
                ('advancePayment', models.FloatField(verbose_name='Advance payment')),
                ('driverName', models.CharField(blank=True, max_length=60, verbose_name='Driver name')),
                ('driverPhone', models.CharField(blank=True, max_length=15, verbose_name='Driver phone')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state', verbose_name='State')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargoes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('can_change_password', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', cargas_aqui.core.managers.UserProfileManager()),
            ],
        ),
    ]
