from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["receiver_name", "phone_number", "address", "detail_address"]
        labels = {
            "receiver_name": "수령인 이름",
            "phone_number": "전화번호",
            "address": "주소",
            "detail_address": "상세 주소",
        }
