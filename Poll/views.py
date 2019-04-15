# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question


# Create your views here.
def index(request):
    the_question = Question.objects.order_by('-pub_date')[:5]
    context = {'the_question': the_question}
    return render(request, 'Poll/index.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'Poll/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Poll/result.html',{'question':question})

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'Poll/detail.html',{'question':question, 'error:message':"Please select a choice"})
    else:
        selected_choice.votes = selected_choice.votes+1
        selected_choice.save()

        return HttpResponseRedirect(reverse('Poll:result', args=(question_id,)))
