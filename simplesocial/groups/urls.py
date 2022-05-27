from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroupsView.as_view(), name='all'), 
    path('new/', views.CreateGroupView.as_view(), name='create'), 
    path('posts/in/<slug:slug>/', views.SingleGroupView.as_view(), name='single'), 
    path('join/<slug:slug>/', views.JoinGroup.as_view(), name='join'), 
    path('leave/<slug:slug>/', views.LeaveGroup.as_view(), name='leave'), 
]