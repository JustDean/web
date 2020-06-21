from django.http import HttpResponse
from django.views import generic

from .models import Question, Answer


def test(request, *args, **kwargs):
	return HttpResponse('ok')


class MainView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'main.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.new()


class QuestionView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'question.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.new()


class IndexedQuestionView(generic.DetailView):

	model = Question
	template_name = 'question_test.html'
	context_object_name = 'question'


class PopularView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'popular.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.popular()
