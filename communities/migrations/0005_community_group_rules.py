# Generated by Django 2.2.5 on 2022-03-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20220308_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='group_rules',
            field=models.ManyToManyField(blank=True, related_name='communities', to='communities.GroupRule'),
        ),
    ]
