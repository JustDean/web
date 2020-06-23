from django.http import HttpResponse
from django.views import generic
from .models import Question, Answer
from .forms import QuestionListForm
from django.shortcuts import resolve_url, get_object_or_404


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
	template_name = 'new.html'
	fields = ['title', 'text', 'author']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(NewQuestion, self).form_valid(form)

	def get_success_url(self):
		id = self.object.pk
		return resolve_url(f'/question/{id}', pk=self.object.pk)


def question(request):

	q1 = Question.objects.all()
	q2 = Answer.objects.all()
	qq = q1.union(q2)
	return get_object_or_404(qq)



class PopularView(generic.ListView):

	model = Question
	paginate_by = 10
	template_name = 'popular.html'
	context_object_name = 'question'

	def get_queryset(self):
		return Question.objects.popular()
