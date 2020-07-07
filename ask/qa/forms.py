from django import forms
from .models import Question, Answer, User


class QuestionListForm(forms.Form):

    search = forms.CharField(required=False,)
    sort_field = forms.ChoiceField(choices=[('title', 'title'), ('rating', 'rating'), ('added_at', 'date')], required=False)


class AskForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = User.objects.get(pk=1)
        question = Question.objects.create(**self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True, label='Type your answer here', strip=True, )
    question = forms.ModelChoiceField(Question.objects.all())

    def __init__(self, *args, **kwargs):  # this sux so much. I hate myself for it. But it works.
        if len(args) >= 2:
            self._question_id = args[1]
        else:
            self._question_id = -1
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = User.objects.get(pk=1)
        self.cleaned_data['question_id'] = self._question_id
        answer = Answer.objects.create(**self.cleaned_data)
        return answer
