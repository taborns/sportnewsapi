# Generated by Django 2.2.1 on 2019-10-20 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportnews', '0003_auto_20191020_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='match',
        ),
        migrations.CreateModel(
            name='PredictionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictionlist', to='sportnews.Match')),
            ],
        ),
        migrations.AddField(
            model_name='prediction',
            name='predictionlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='sportnews.PredictionList'),
            preserve_default=False,
        ),
    ]
