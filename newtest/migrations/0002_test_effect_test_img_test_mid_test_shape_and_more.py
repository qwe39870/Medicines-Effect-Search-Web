# Generated by Django 4.2.6 on 2023-11-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='effect',
            field=models.CharField(default=222, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='img',
            field=models.CharField(default=222, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='mid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='shape',
            field=models.CharField(default=222, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='sideffect',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='type',
            field=models.CharField(default=222, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='usee',
            field=models.CharField(default=222, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='color',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]