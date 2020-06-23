from django import forms


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


# class NewQuestionForm(forms.Form):
#
#     title = forms.CharField(max_length=255)
#     text = forms.CharField(widget=forms.Textarea)
