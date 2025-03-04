from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TrainerAppIvan_Backend.common.urls')),
    path('account/', include('TrainerAppIvan_Backend.account.urls')),
    path('cart/', include('TrainerAppIvan_Backend.cart.urls')),
    path('product/', include('TrainerAppIvan_Backend.product.urls')),
]
