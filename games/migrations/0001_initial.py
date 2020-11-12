# Generated by Django 3.1.3 on 2020-11-12 03:26

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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('admins', models.ManyToManyField(related_name='games_admining', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='games_playing', to=settings.AUTH_USER_MODEL)),
                ('serverIdentity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games_running', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
