from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='site-home'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/new/', views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', views.EventUpdateView.as_view(), name='event-update'),
    path('join/<int:pk>/', views.join_event, name='join-event')
]