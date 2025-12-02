from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add/<int:product_id>/", views.add_to_cart, name="add"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove"),
    path("create/", views.create_order, name="create_order"),
    path("complete/<int:order_id>/", views.order_complete, name="order_complete"),
    path("history/", views.order_history, name="order_history"),

]
