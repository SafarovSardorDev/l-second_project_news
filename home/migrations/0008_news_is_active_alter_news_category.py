# Generated by Django 4.2.7 on 2023-11-21 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_contactpersonal_rename_name_contact_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.category'),
        ),
    ]
