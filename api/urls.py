from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.QuestionAPI.as_view()),
    path('api/<int:pk>', views.QuestionRetrieveUpdateDestroyAPIView.as_view()),
    path('list/', views.list_questionnaire, name='list_questionnaire'),
    path('', views.index, name='index')
]
