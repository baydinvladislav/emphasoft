from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from .models import Profile


class ProfileList(ListView):
    """
    Provides all registered users.
    """
    model = User
    template_name = 'profiles/profile_list.html'
    context_object_name = 'users'
    paginate_by = 10


class ProfileView(DetailView):
    """"
    Provides a specific user by pk.
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'


class ProfileUpdate(UpdateView):
    """
    Creates form for update specific user.
    """
    model = Profile
    fields = ['first_name', 'last_name', 'patronymic', 'profile_picture', 'bio']
    template_name = 'profiles/profile_form.html'
    success_url = ''
