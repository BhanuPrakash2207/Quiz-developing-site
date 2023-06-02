from django.shortcuts import render

def index(request):
    return render(request,'quiz/base.html')