# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_prometheus.models import ExportModelOperationsMixin


@python_2_unicode_compatible
#class Question(models.Model):
class Question(ExportModelOperationsMixin('question'), models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


@python_2_unicode_compatible
#class Choice(models.Model):
class Choice(ExportModelOperationsMixin('choice'), models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
