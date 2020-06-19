from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render  # cool stuff. Try it

from .models import Question, Answer


def test(request, *args, **kwargs):
	return HttpResponse('ok')


class MainView(generic.ListView):

	model = Question
	template_name = 'main.html'


class QuestionView(generic.ListView):

	model = Question
	template_name = 'question.html'


class IndexedQuestionView(generic.DetailView):

	model = Question
	template_name = 'question_test.html'
	context_object_name = 'question'
