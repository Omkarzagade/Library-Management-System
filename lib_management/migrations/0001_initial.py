# Generated by Django 4.2.6 on 2023-10-09 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=25)),
                ('isbn', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=25)),
                ('pages', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('outstanding_debt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('rent_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib_management.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib_management.member')),
            ],
        ),
    ]
