# Generated by Django 3.1.2 on 2021-06-11 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210310_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=1000)),
                ('cat_img', models.ImageField(upload_to='shop/cats')),
                ('cat1', models.CharField(max_length=1000)),
                ('cat2', models.CharField(max_length=2000)),
                ('cat4', models.CharField(max_length=9000)),
                ('cat5', models.CharField(max_length=9000)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='videocomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shareitsuser',
            name='UserSubs',
        ),
        migrations.RemoveField(
            model_name='shareitsuser',
            name='Userposts',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.DeleteModel(
            name='VideoComment',
        ),
    ]