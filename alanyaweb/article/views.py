from django.http import request
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse
from .forms import Article, ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):

    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})


def index(request):
    # return HttpResponse("ana sayfa")    #1.yöntem
    context = {
        "number1":10,
        "number2":20,
        "numbers":[1,2,3,4,5]
    }

    return render(request,"index.html",context)     #2.yöntem


def about(request):

    return render(request,"about.html")


def detail(request,id):

    return HttpResponse("Detail" + str(id))

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)

    return render(request,"dashboard.html",{"articles":articles})

@login_required   # login yapılıp yapılmadığını kontrol eder
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user

        article.save()
        messages.success(request,"makale başarıyla oluşturuldu.")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})


def detail(request,id):
    # article = Article.objects.filter(id = id).first() #first yazmazsak tüm articles lar gelir ve hata alırız. 
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})


@login_required
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user

        article.save()
        messages.success(request,"makale başarıyla değiştirildi.")
        return redirect("index")

    return render(request,"update.html",{"form":form})


@login_required
def deleteArticle(request,id):

    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"makale başarıyla silindi")

    return redirect("article:dashboard")          #article altınfaki dashboard

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))




