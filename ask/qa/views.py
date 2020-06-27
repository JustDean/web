from django.http import HttpResponse
from django.views import generic
from .models import Question, Answer
from .forms import QuestionListForm
from django.shortcuts import resolve_url


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
	template_name = 'all_questions.html'
	context_object_name = 'question'

	def dispatch(self, request, *args, **kwargs):
		self.form = QuestionListForm(request.GET)
		self.form.is_valid()
		return super(QuestionView, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		queryset = Question.objects.all()
		if self.form.cleaned_data.get('search'):
			queryset = queryset.filter(title__icontains=self.form.cleaned_data['search'])
		if self.form.cleaned_data.get('sort_field'):
			queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
		else:
			queryset = Question.objects.new()
		return queryset

	def get_context_data(self, **kwargs):
		context = super(QuestionView, self).get_context_data(**kwargs)
		context['form'] = self.form
		return context


class NewQuestion(generic.CreateView):

	model = Question
	template_name = 'ask.html'
	fields = ['title', 'text', 'author']
	# user validation
	# def form_valid(self, form):
	# 	form.instance.author = self.request.user
	# 	return super(NewQuestion, self).form_valid(form)

	def get_success_url(self):
		id_x = self.object.pk
		return resolve_url('/question/{}'.format(id_x), pk=id_x)


class TheQuestion(generic.DetailView):

	model = Question
	template_name = 'the_question.html'

	def get_context_data(self, **kwargs):
		context = super(TheQuestion, self).get_context_data(**kwargs)
		context['answers'] = Answer.objects.filter(question_id=self.object.id)
		return context


class PopularView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'popular.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.popular()


class NewAnswer(generic.CreateView):

	model = Answer
	template_name = 'the_question.html'
	fields = ['text']
	context_object_name = 'answer_form'

	def get_success_url(self):
		id = self.object.question_id
		return resolve_url('/question/{}'.format(id), pk=self.object.pk)



