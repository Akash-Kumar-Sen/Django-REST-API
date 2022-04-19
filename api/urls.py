from django.urls import path

# Auth token for rest framework
from rest_framework.authtoken.views import obtain_auth_token

# Import all views
from .views import *

urlpatterns=[
    path('token/', obtain_auth_token, name='obtain-token'),

    # List
    path('list/',BoxItemList.as_view(),name='list'),

    # Create
    path('add-new/',CreateBoxItem.as_view(),name='add-new'),

    # Update
    path('update/<int:pk>/',UpdateBoxItem.as_view(),name='update'),

    # Delete
    path('delete/<int:pk>/',DeleteBoxItem.as_view(),name='delete'),
]