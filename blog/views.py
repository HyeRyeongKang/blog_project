from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

# Create your views here.
def home(request):
    blogs=Blog.objects
    # 블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator=Paginator(blog_list, 4)
    # request된 페이지가 뭔지를 알아내고(request페이지(키 값이 page인)를 page 변수에 담아내고)
    page=request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해줌
    posts=paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail':detail})

def new(request):
    return render(request, 'new.html')

# 입력 받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() # 객체 내용을 데이터베이스에 저장
    # 해당 url로 넘겨라
    # str(blog.id) : 문자열로 형변환
    # redirect는 url을 담음. 
    # render는 html에 데이터를 담아 처리하고 싶을 때
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 1. 입력되는 내용을 처리하는 기술 : POST
    if request.method=='POST':
        form=BlogPost(request.POST) # 입력된 내용 담아줌
        if form.is_valid():
            post=form.save(commit=False)    # 저장하지 않고 model객체 가져오기
            post.pub_date=timezone.now()
            post.save() # 시간까지 넣은 후 저장
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 : GET
    else:
        form=BlogPost()
        return render(request, 'new.html', {'form':form})
