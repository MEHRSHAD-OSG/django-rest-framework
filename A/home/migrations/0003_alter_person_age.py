# Generated by Django 5.0.6 on 2024-07-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
