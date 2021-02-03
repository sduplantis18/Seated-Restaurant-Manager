"""Defines URL patterns for learning_logs"""

from os import name, stat
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
    # Detail page for an Entry(restaurant)
    path('entry/<int:entry_id>/', views.entry, name='entry'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name ='new_topic'),
    # Page for adding a new entry(Restaurant)
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for updating an existing entry(Restaurant)
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for deleting a Topic(venue)
    path('delete/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    # Page for adding a new menu 
    path('new_menu/<int:entry_id>/', views.new_menu, name='new_menu'),
    # Page for a menu
    path('menu/<int:menu_id>/', views.menu, name='menu'),
    # Page for a new menu_item
    path('new_menu_item/<int:menu_id>/', views.new_menu_item, name='new_menu_item'),
    # Page for editing a menu item
    path('edit_menu_item/<int:menu_item_id>/', views.edit_menu_item, name='edit_menu_item'),
    # Display a dashboard for the vendor
    path('my_restaurant/', views.my_restaurant, name='my_restaurant'),
    # Display Detailed order view for managers
    path('manage_orders/<int:entry_id>/', views.manage_orders, name='manage_orders'),
    # Display form to update an order status
    path('update_status/<int:order_id>/', views.update_order_status, name='update_status'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

