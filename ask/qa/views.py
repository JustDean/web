from django.http import HttpResponse
from django.views import generic

from .models import Question, Answer


def test(request, *args, **kwargs):
	return HttpResponse('OK')


class QuestionView(generic.ListView):

	model = Question
	template_name = 'qa/Questions.html'
