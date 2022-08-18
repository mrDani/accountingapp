from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('team/', views.team, name="team"),
    path('frequent_question/', views.frequent_question, name="faqs"),
    path('team_info/', views.team_info, name="team_info"),
]
