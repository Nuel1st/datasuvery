from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('upload_media/', views.upload_media, name='upload_media'),
    path('start_point/create/', views.create_start_point, name='create_start_point'),
    path('end_point/create/', views.create_end_point, name='create_end_point'),
]


