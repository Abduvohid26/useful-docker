# Generated by Django 5.0.6 on 2024-07-10 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_test_subject_remove_question_test_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='main.category'),
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answers', to='main.variant')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_results', to='main.result')),
                ('selected_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_answers', to='main.variant')),
            ],
        ),
    ]
