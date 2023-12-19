from django.urls import path, include
from .views import register, profile, update_profile, registration_success, registration_error, registration_check_email

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('registration_success/', registration_success, name='registration_success'),
    path('registration_error/', registration_error, name='registration_error'),
    path('registration_check_email/', registration_check_email, name='registration_check_email'),
]
