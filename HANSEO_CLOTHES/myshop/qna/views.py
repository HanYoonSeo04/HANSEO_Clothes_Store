from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QnA
from django.utils import timezone


@login_required
def qna_list(request):
    qnas = QnA.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "qna/list.html", {"qnas": qnas})


@login_required
def qna_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        question = request.POST["question"]

        QnA.objects.create(
            user=request.user,
            title=title,
            question=question
        )
        return redirect("qna:list")

    return render(request, "qna/create.html")


@login_required
def qna_detail(request, qna_id):
    qna = get_object_or_404(QnA, id=qna_id, user=request.user)
    return render(request, "qna/detail.html", {"qna": qna})
