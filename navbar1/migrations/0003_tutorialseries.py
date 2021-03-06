# Generated by Django 3.0.8 on 2021-10-25 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('navbar1', '0002_update_matches'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_ans', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('match_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='navbar1.update_matches')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
