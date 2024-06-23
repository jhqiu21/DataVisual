# set the urls of visual logs
from django.urls import path
# import urls to views.py
from .import views

app_name = 'visual_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # detail page of a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # add new topic form
    path('new_topic/', views.new_topic, name='new_topic'),
    # page to add new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page to edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # delete entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # delete topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]

