from django.urls import path, include
from .views import UserCreateView, validate_username

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', UserCreateView.as_view()),
    path('ajax/accounts/validate', validate_username, name='validate_username'),
]