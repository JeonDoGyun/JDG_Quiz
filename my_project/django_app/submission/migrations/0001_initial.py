# Generated by Django 5.1.4 on 2025-04-20 09:41

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('quiz_submission_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('snapshot', models.JSONField()),
                ('score', models.PositiveIntegerField()),
                ('submitted_at', models.DateTimeField(auto_now=True, null=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='quiz.quiz')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'submissions',
            },
        ),
        migrations.CreateModel(
            name='SubmissionAnswer',
            fields=[
                ('submission_answer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_correct', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('quiz_submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='submission.submission')),
                ('selected_choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.choice')),
            ],
            options={
                'db_table': 'submission_answers',
            },
        ),
    ]
