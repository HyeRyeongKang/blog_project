from django.shortcuts import render, redirect

# 외울필요 없음
# user에 대한 클래스, 권한에 대한 내용 가져옴
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['pwd1']==request.POST['pwd2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['pwd1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pwd']
        # 회원이 맞는지 확인하는 함수
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)   # 로그인 해줌
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')