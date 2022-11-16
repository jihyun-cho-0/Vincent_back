# Generated by Django 4.1.3 on 2022-11-16 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=25)),
                ('filter_image', models.ImageField(upload_to='filter/%Y/%m/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
