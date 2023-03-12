# Generated by Django 4.1.7 on 2023-03-11 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qantity', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.signup')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]