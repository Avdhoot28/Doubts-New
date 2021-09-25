# Generated by Django 3.1.7 on 2021-04-11 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doubtsBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubt',
            name='image',
            field=models.ImageField(null=True, upload_to='doubt_pics'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='answer_pics')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doubt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doubtsBlog.doubt')),
            ],
        ),
    ]
