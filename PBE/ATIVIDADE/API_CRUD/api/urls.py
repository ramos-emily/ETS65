from django.urls import path
from .views import UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
]
    