# Generated by Django 2.2.5 on 2022-03-07 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0002_community_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='host',
        ),
        migrations.AddField(
            model_name='community',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='communities', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=140, verbose_name='이름(name)'),
        ),
        migrations.AlterField(
            model_name='community',
            name='people',
            field=models.IntegerField(verbose_name='인원(people)'),
        ),
    ]
