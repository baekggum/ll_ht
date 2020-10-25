# Generated by Django 3.1.1 on 2020-10-24 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=20)),
                ('admin_password', models.CharField(max_length=20)),
                ('admin_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QR_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ImageField(blank=True, upload_to='')),
                ('product_name', models.CharField(max_length=20)),
                ('product_code', models.CharField(max_length=20)),
                ('product_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField()),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='receipt')),
                ('content', models.TextField()),
                ('approval_status', models.CharField(max_length=10)),
                ('qr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.qr_code')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
    ]
