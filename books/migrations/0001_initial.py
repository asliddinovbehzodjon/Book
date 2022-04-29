# Generated by Django 4.0.4 on 2022-04-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitoblar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kitob nomini kiriting', max_length=1000, verbose_name='Kitob nomini kiriting')),
                ('author', models.TextField(help_text='Kitob muallifini yozing', verbose_name='Kitob muallifini yozing')),
                ('description', models.TextField(help_text='Kitob haqida yozing', verbose_name='Kitob haqida yozing')),
                ('image', models.ImageField(default='https://png.pngtree.com/element_our/20190602/ourlarge/pngtree-blue-book-decoration-illustration-image_1387046.jpg', upload_to='images')),
                ('file', models.FileField(upload_to='books')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('downloaded', models.IntegerField(default=1)),
                ('user', models.ForeignKey(default='Kitobxon', on_delete=django.db.models.deletion.SET_DEFAULT, to='readers.kitobxon')),
            ],
            options={
                'verbose_name': 'Kitob ',
                'verbose_name_plural': 'Kitoblar ',
                'db_table': 'Kitoblar',
            },
        ),
    ]
