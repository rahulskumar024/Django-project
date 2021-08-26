from polls.models import Question
from django.shortcuts import render

from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, question_id):
    return HttpResponse(f"question_id {question_id}")
def results(request, question_id):
    response=f"resultfor question_id {question_id}"
    return HttpResponse(response)
def vote(request, question_id):
    return HttpResponse("voting on question id")

def questions(request):
    questions = Question.objects.all()
    # output=[]
    # for q in questions:
    #     output.append(q.question_text)
    #output=",".join(output)
    context = {"questions": questions,"name":"Rahul"}
    
    return render(request, "polls/index.html", context)
    
