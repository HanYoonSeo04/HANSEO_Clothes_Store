from django.shortcuts import render, redirect, get_object_or_404
from .models import Qna
from django.utils import timezone

def qna_list(request):
    qnas = Qna.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "qna/list.html", {"qnas": qnas})

def qna_create(request):
    if request.method == "POST":
        Qna.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            category=request.POST.get("category"),
            content=request.POST.get("content"),
            image=request.FILES.get("image"),
        )
        return redirect("qna:list")

    return render(request, "qna/create.html")
