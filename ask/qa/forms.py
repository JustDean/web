from django import forms
from .models import Question


class QuestionListForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=[('title', 'title'), ('rating', 'rating'), ('added_at', 'date')], \
                 required=False)

    # def clean(self):    # custom validation for all forms
    #     raise forms.ValidationError('Why? Because I can.')

    # def clean_search(self):     # custom validation for 'search' form
    #     search = self.cleaned_data.get('search')
    #     raise forms.ValidationError('Man, search yourself!')
    #     return search


class AskForm(forms.Form):

    title = forms.CharField(required=True)
    text = forms.CharField(required=True, widget=forms.Textarea)


class AnswerForm(forms.Form):

    text = forms.CharField(required=True, widget=forms.Textarea)
    # question = forms.ChoiceField(choices=Question.objects.all())




