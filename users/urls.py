from django.urls import path
from .views import UserEditView, PasswordsChangeView, password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/',UserEditView.as_view(), name='profile'),
    path('password/',PasswordsChangeView.as_view()),
    path('password_success', password_success, name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='showprofile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),


]