from django.db import models

from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    pass


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=0)
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='question_author'
    )
    likes = models.ManyToManyField(
        User,
        related_name='question_like'
    )


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
