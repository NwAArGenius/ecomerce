from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:product_id>/', views.cart_add,  name="add"),
    path('remove/<str:product_id>/', views.cart_remove,  name="remove"),
    path('cart_details/', views.cart_detail, name='cart_detail'),
]
