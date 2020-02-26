from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
import random
# Create your views here.

def index(request):
    
    return render(request,"index.html",{"round":"1"})

def questions(request):
    round = request.GET.get("round")
    if round == "1":
        i = random.randint(1,2)
    else:
        i = 3
    request.session["round"]=round
    question = Question.objects.filter(set=i)
    result = []
    for q in question:
        temp = {"id":q.no,"question":q.question,"options":[{"a":q.a,"b":q.b,"c":q.c,"d":q.d}],"answer":q.answer,"score":0,"status":""}
        result.append(temp)
    return JsonResponse(result,safe=False)

def start_exam(request):

    name = request.GET.get("name")
    reg = request.GET.get("reg")
    request.session["name"] = name
    request.session["reg"] = reg
    return JsonResponse(True,safe=False)

def submit(request):
    scr = request.GET.get("scr")
    if request.session["round"] == "1":
        result = Result(score=scr,name=request.session["name"],registration_no=request.session["reg"])
    else:
        result = Result.objects.get(registration_no = request.session["reg"])
        result.score2 = scr
    result.save()
    return JsonResponse(True,safe=False)

def results(request):
    result = Result.objects.extra(
    select={'fieldsum':'score + score2'},
    order_by=('fieldsum',)
)
    return render(request,"results.html",{"results":result})

def round2(request):
    
    return render(request,"index.html",{"round":"2"})
