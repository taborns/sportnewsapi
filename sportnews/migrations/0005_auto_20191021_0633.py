# Generated by Django 2.2.1 on 2019-10-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportnews', '0004_auto_20191020_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('created_at',), 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='standing',
            options={'ordering': ('rank',)},
        ),
        migrations.AddField(
            model_name='standing',
            name='goal',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standing',
            name='played',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standing',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
