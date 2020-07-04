from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Question, Answer, User
from .forms import QuestionListForm, AskForm, AnswerForm
from django.shortcuts import render


def test(request, *args, **kwargs):
	return HttpResponse('ok')


class MainView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'main.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.order_by('-added_at')


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
			queryset = Question.objects.order_by('-added_at')
		return queryset

	def get_context_data(self, **kwargs):
		context = super(QuestionView, self).get_context_data(**kwargs)
		context['form'] = self.form
		return context


class PopularView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'popular.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.order_by('-rating')


def the_question(request, *args, **kwargs):
	question_url = request.path.lstrip('/question/')  # no practical need for that
	question_id = request.path.lstrip('/question/').rstrip('/')
	if request.method == 'POST':
		form = AnswerForm(request.POST, question_id)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/question/{}'.format(question_url))
	else:
		question = Question.objects.get(pk=question_id)
		answers = Answer.objects.filter(question_id=question_id)
		form = AnswerForm()
		return render(request, 'the_question.html', {
			'question': question,
			'answers': answers,
			'form': form,
		})


def ask_question(request, *args, **kwargs):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = question.pk
			return HttpResponseRedirect('/question/{}'.format(url))
	else:
		form = AskForm()
		return render(request, 'ask.html', {
			'form': form,
		})
