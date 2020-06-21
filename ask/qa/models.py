from django.db import models

from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    use_in_migrations = False

    def new(self):
        return self.order_by('-date')

    def popular(self):
        return self.oreder_by('-rating')


class Question(models.Model):
    objects = QuestionManager()

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering = ('-added_at', )


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
