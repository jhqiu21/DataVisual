# set the urls of visual logs
from django.urls import path, include
# import urls to views.py
from .import views

app_name = 'visual'
urlpatterns = [
    # include default login url
    path('', include('django.contrib.auth.urls')),
    # Data analysis
    path('upload_file/', views.upload_file, name='upload_file'),
    # path('view_plot/', views.view_plot, name='view_plot'),
]

