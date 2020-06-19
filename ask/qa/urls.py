from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question'),
    path('<pk>', views.IndexedQuestionView.as_view(), name='indexed_question'), # !!! ues pk instead of id or whatever!
]
