from django.urls import path

from TrainerAppIvan_Backend.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]