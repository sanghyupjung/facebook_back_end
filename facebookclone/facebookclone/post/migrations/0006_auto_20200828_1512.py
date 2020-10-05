# Generated by Django 3.1 on 2020-08-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='post.Tag'),
        ),
    ]
