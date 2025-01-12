from django.urls import path
from . import views

urlpatterns = [
    path('upload-files/', views.upload_view, name='upload_view'),
    path('add-data/', views.add_data, name='add_data'),
    path('check-data/', views.check_data_view, name='check_data'),
]