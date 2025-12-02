from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력하세요'})
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력하세요'})
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 한 번 더 입력하세요'})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UserEditForm(UserChangeForm):
    password = None  # 패스워드 필드 숨김

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]