from django.contrib import admin
from .models import QnA
from django.utils import timezone


class QnaAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_at", "answered_at")
    search_fields = ("user__username", "title")
    readonly_fields = ("created_at", "answered_at")

    # 관리자에서 답변 입력 시 answered_at 자동 생성
    def save_model(self, request, obj, form, change):
        if obj.answer and not obj.answered_at:
            obj.answered_at = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(QnA, QnaAdmin)
