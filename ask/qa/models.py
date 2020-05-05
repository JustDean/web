from django.db import models

from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    pass


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-date')
    
    def popular(self):
        return self.oreder_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, name='date')
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
