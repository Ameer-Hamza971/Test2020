from django.shortcuts import render, redirect
from .models import MathTester, MathAnswers
# Create your views here.

def mathtest(request):
    question = MathTester.objects.all()
    if request.method == 'POST':
        name = request.POST['std_name']
        rollNo = request.POST['rollNo']
        ans_no_1 = request.POST['MathAns1']
        ans_no_2 = request.POST['MathAns2']
        ans_no_3 = request.POST['MathAns3']
        ans_no_4 = request.POST['MathAns4']
        ans_no_5 = request.POST['MathAns5']
        MathAnswer = MathAnswers(name=name, rollNo=rollNo, ans_no_1=ans_no_1, ans_no_2=ans_no_2, ans_no_3=ans_no_3, ans_no_4=ans_no_4, ans_no_5=ans_no_5)
        MathAnswer.save()
        return redirect('/')
    else:
        return render(request, 'mathtest.html', {'question': question})


def teacherDisplay(request):
    allAns = MathAnswers.objects.all()
    return render(request, 'teacher.html', {'allAns': allAns})