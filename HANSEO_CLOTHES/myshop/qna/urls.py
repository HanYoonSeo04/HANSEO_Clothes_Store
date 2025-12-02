from django.urls import path, include
from . import views

app_name = "qna"

urlpatterns = [
    path("list/", views.qna_list, name="list"),
    path("create/", views.qna_create, name="create"),
    path("products/", include("products.urls")),
    path("reviews/", include("reviews.urls")),
    path("qna/", include("qna.urls")),

]
