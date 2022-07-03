from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Question, Questionnaire
from . import serializer


class QuestionAPI(ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = serializer.QuestionnaireSerializer

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


def index(request):
    return render(request, 'index.html')
