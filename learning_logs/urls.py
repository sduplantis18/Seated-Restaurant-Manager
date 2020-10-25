"""Defines URL patterns for learning_logs"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a simple topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name ='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for updating an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)