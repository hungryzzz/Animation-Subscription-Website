# Generated by Django 2.0.4 on 2018-05-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='img')),
                ('name', models.CharField(max_length=40)),
                ('pub_time', models.DateField()),
                ('update_time', models.CharField(max_length=60)),
                ('style', models.CharField(max_length=30, null=True)),
                ('tag1', models.CharField(max_length=30, null=True)),
                ('tag2', models.CharField(max_length=30, null=True)),
                ('va1', models.CharField(max_length=40, null=True)),
                ('va2', models.CharField(max_length=40, null=True)),
                ('va3', models.CharField(max_length=40, null=True)),
                ('va4', models.CharField(max_length=40, null=True)),
                ('state', models.CharField(max_length=40)),
                ('link', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('id_num', models.CharField(max_length=20)),
                ('pw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('ani_name', models.CharField(max_length=40)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pw', models.CharField(max_length=20)),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('legal', models.BooleanField()),
            ],
        ),
    ]
