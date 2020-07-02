from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question'),
    path('<pk>', views.the_question),
    path('<pk>/', views.the_question),
]
