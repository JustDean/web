from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name='question_like'
    )

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-added_at', )

    def __str__(self):
        return '{} by {} id{}'.format(self.question.title, self.author.username, str(self.author.id))
