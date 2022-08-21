"""Define URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page thatt shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry')
]
