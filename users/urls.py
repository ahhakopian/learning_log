"""Определяет схемы URL для пользователей"""
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('learning_logs:index')), name='logout'),
    # Страница регистрации
    path('register/', views.register, name='register'),

]