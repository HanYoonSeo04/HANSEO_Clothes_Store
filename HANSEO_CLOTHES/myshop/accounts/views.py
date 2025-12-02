from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserEditForm

# 회원가입
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect("accounts:mypage")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


# 로그인
def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:mypage")

    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("accounts:mypage")
        else:
            error = "아이디 또는 비밀번호가 올바르지 않습니다."

    return render(request, "accounts/login.html", {"error": error})


# 로그아웃
def logout_view(request):
    logout(request)
    return redirect("/")


# 마이페이지
@login_required
def mypage(request):
    return render(request, "accounts/mypage.html")


# 내 정보 수정
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.address = request.POST.get("address")
        profile.save()
        return redirect("accounts:mypage")

    return render(request, "accounts/edit_profile.html", {"profile": profile})
