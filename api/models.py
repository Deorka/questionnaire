from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)
    correct_answers = models.CharField(max_length=255, help_text='Write answers through ;')
    incorrect_answers = models.CharField(max_length=255, help_text='Write answers through ;')

    def __str__(self):
        return self.question


class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.questionnaire_name
