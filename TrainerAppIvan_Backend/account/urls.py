from django.urls import path

from TrainerAppIvan_Backend.account import views

urlpatterns = [
    path('details/', views.AccountDetailView.as_view(), name='account-detail'),
]