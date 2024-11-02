from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', auth_views.LoginView.as_view(template_name='tournament/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('fixtures/', views.fixtures, name='fixtures'),
    path('standings/', views.standings, name='standings'),
    path('generate-fixtures/', views.generate_fixtures, name='generate_fixtures'),  # New URL
]
