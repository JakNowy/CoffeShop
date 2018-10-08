from django.urls import path
import shop.views as shop_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='coffeshop/home.html'), name='home'),
    path('register/', shop_views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='coffeshop/logout.html'), name='logout'),
    path('providers/', shop_views.ProvidersView.as_view(), name='providers'),
    path('providers/new', shop_views.ProviderCreationView.as_view(), name='provider-new'),
    path('providers/<provider>', shop_views.ProviderDetailView.as_view(), name='provider-detail'),
    path('offers/<offer_id>', shop_views.OfferDetailView.as_view(), name='offer-detail'),
    path('offers/', shop_views.OffersView.as_view(), name='offers'),
    path('thanks/<int:user_id>', shop_views.ThanksView.as_view(), name='thanks'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)