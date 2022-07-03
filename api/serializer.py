from rest_framework import serializers
from .models import Questionnaire, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question', 'correct_answers', 'incorrect_answers')


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Questionnaire
        fields = ('questionnaire_name', 'questions',)
