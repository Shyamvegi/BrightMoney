# Generated by Django 3.2.10 on 2021-12-18 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plaidApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=150)),
                ('item_id', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Transaction',
            new_name='AccountDetails',
        ),
        migrations.RenameModel(
            old_name='Log',
            new_name='LogsModel',
        ),
        migrations.RenameModel(
            old_name='Account',
            new_name='TransactionsModel',
        ),
        migrations.DeleteModel(
            name='TokenItem',
        ),
    ]
