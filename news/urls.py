from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
]
