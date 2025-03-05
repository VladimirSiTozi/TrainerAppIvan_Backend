from django.contrib import admin
from django.urls import path, include

from TrainerAppIvan_Backend.account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('', include('TrainerAppIvan_Backend.common.urls')),
    path('account/', include('TrainerAppIvan_Backend.account.urls')),
    path('cart/', include('TrainerAppIvan_Backend.cart.urls')),
    path('product/', include('TrainerAppIvan_Backend.product.urls')),
]
