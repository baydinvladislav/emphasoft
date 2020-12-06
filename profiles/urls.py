from django.urls import path, include
from .views import ProfileList, ProfileView, ProfileUpdate


urlpatterns = [
    # List of all created users.
    path('', ProfileList.as_view(), name='profiles_list'),
    # View page of specific user.
    path('<int:pk>/', ProfileView.as_view(), name='profile_detail'),
    # Update page of specific user.
    path('edit/<int:pk>/', ProfileUpdate.as_view(), name='profile_form'),
    # Social-auth library connection.
    path('social-auth/', include('social_django.urls', namespace='social')),
]
