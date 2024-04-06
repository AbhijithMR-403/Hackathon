from django.shortcuts import render

# Create your views here.




def login(request):
    return render(request,'user/login.html')

def signup(request):
    return render(request,'user/signup.html')


def quiz(request):
    return render(request,'user/quiz.html')