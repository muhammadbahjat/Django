from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
 #   return render(request, 'polls/index.html')

#def detail(request, question_id):
 #   return render(request, 'polls/detail.html', {'question_id': question_id})

def index(request):
    return HttpResponse("Awsome Good Job! This is the Index Page of our polls application")


def detail(request):
    print('Hellooooo')
    return HttpResponse("This is the detail view of the question:aajajxjnajn")

def results(request, question_id):
    return HttpResponse("there are the result of the question: %s " % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on the question: %s" % question_id)
