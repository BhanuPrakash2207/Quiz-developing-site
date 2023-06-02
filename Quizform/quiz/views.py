from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .addform import *
import pytz
from rest_framework.views import APIView
from rest_framework import status,permissions
from .models import *
from .serializers import QuesSerializer
from datetime import datetime


class QuesListAPIView(APIView):
    permissions_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        ques=Ques.objects.filter(user=request.user.id)
        serializer=QuesSerializer(ques,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        data={'task':request.data.get('task'),
              'completed':request.data.get('completed'),
              'user':request.user.id}
        serializer=QuesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    if request.method=='POST':
        print(request.POST)
        questions=Ques.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(q.ques)
            print(q.ans)
            print(q.start_time)
            print(type(q.start_time))
            print(q.end_time)
            print(type(datetime.now()))
            print()

            if q.ans == request.POST.get(q.ques):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent=(score/(total*10))*100
        context={
            'score':score,
            'time':request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        question=Ques.objects.all()
        context={
            'questions':question
        }
        questions = Ques.objects.all()
        for q in questions:
            st_tm = q.start_time.replace(tzinfo=pytz.utc)
            end_tm = q.end_time.replace(tzinfo=pytz.utc)
            curr_tm = datetime.now().replace(tzinfo=pytz.utc)
            if st_tm <= curr_tm <= end_tm:
                return render(request,'Quiz/home.html',context)
            else:
                return render(request,'Quiz/result.html',context)


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform(request)
        if (request.method == 'POST'):
            form = addQuestionform(request.POST)
            Question=request.POST.get('Question','')
            op1=request.POST.get('option1','')
            op2=request.POST.get('option2','')
            op3=request.POST.get('option3','')
            op4=request.POST.get('option4','')
            ans=request.POST.get('answer','')
            start_time=request.POST.get('start_time','')
            end_time=request.POST.get('end_time','')
            Quest=Ques(ques=Question,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans,start_time=start_time,end_time=end_time)
            Quest.save()
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'Quiz/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'Quiz/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
# Create your views here.
