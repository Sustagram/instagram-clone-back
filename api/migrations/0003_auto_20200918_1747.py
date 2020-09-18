# Generated by Django 3.1.1 on 2020-09-18 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200918_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post_id',
            field=models.OneToOneField(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='rbr',
            name='reply_id',
            field=models.ForeignKey(db_column='reply_id', on_delete=django.db.models.deletion.CASCADE, to='api.reply'),
        ),
        migrations.AlterField(
            model_name='rbr',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post_id',
            field=models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='following_id',
            field=models.ForeignKey(db_column='following_id', on_delete=django.db.models.deletion.CASCADE, related_name='following_set', to='api.user'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_set', to='api.user'),
        ),
    ]
