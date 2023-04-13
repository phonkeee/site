from django.urls import path
from . import views


urlpatterns = [
    path('',views.homePage, name='homepage'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('', views.aboutPage, name='aboutpage'),
]