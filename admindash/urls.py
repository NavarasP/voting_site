from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    # Include the admin dashboard URL
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Custom Admin URLs for Voters
    path('add_voter/', views.add_voter, name='add_voter'),
    path('edit_voter/<int:voter_id>/', views.edit_voter, name='edit_voter'),
    path('delete_voter/<int:voter_id>/', views.delete_voter, name='delete_voter'),
    

    # Custom Admin URLs for Voting Sessions
    path('create_session/', views.create_session, name='create_session'),
    path('edit_session/<int:session_id>/', views.edit_session, name='edit_session'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),

]