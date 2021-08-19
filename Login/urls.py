from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='home'),
    path("them/", views.them, name="them"),
    path("sua/<str:pk>", views.sua, name="sua"),
    path("xoa/<str:pk>", views.xoa, name="xoa")
]
