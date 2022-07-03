from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Question, Questionnaire
from . import serializer


class QuestionAPI(ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = serializer.QuestionnaireSerializer
    # permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Questionnaire Added !",
                         "data": serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.QuestionnaireSerializer

    def get_queryset(self):
        return Questionnaire.objects.filter(id=self.kwargs.get('pk', None))


def list_questionnaire(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'list_questionnaire.html', {'questionnaire': questionnaires})
    """
    Функция отображения для домашней страницы сайта.
    
    # Генерация "количеств" некоторых главных объектов
    num_questionnaire = Questionnaire.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits': num_visits},  # num_visits appended
    )
    """


def index(request):
    return render(request, 'index.html')
