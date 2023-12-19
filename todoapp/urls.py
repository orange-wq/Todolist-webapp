from django.urls import path
from .views import *


app_name = 'todoapp'
urlpatterns = [
    path('', index, name='index'),
    path('dates/', dates, name='dates'),
    path('date/<int:date_id>/', date, name='date'),
    path('new_date/', new_date, name='new_date'),
    path('new_entry/<int:date_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
    path('update_entry/<int:entry_id>/', update_entry, name='update_entry'),
    path('completed_dates/', completed_dates, name='completed_dates'),
    path('delete_entry/<int:entry_id>/', delete_entry, name='delete_entry'),
    path('delete_date/<int:date_id>/', delete_date, name='delete_date'),
    path('upload_image/<int:entry_id>/', upload_image, name='upload_image'),
    path('delete_image/<int:entry_id>/', delete_image, name='delete_image'),
]
