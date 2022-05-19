# Generated by Django 3.2.9 on 2022-05-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BanerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='baners/')),
                ('add_link', models.URLField()),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Картинка для банера',
                'verbose_name_plural': 'Картинки для банера',
                'ordering': ['-created'],
            },
        ),
    ]
