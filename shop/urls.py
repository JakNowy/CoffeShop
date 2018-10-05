from django.urls import path
import shop.views as shop_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='coffeshop/home.html'), name='home'),
    path('register/', shop_views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='coffeshop/logout.html'), name='logout'),
    path('providers/', shop_views.ProvidersView.as_view(), name='providers'),
    path('offers/', shop_views.OffersView.as_view(), name='offers'),
]