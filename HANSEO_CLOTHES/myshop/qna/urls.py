from django.urls import path
from . import views

app_name = "qna"

urlpatterns = [
    path("list/", views.qna_list, name="list"),
    path("create/", views.qna_create, name="create"),
    path("<int:qna_id>/detail/", views.qna_detail, name="detail"),
    
]
