from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import register_confirm_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('todoapp.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/confirm/<str:uidb64>/<str:token>/', register_confirm_view, name='register_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

