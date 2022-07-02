from rest_framework import serializers
from .models import Questionnaire, Question


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'
