from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.shortcuts import render
from .forms import CustomUserCreationForm


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')


def validate_username(request):
    username = request.GET.get('username', None)
    is_taken = False
    if(get_user_model().objects.filter(email__iexact=username).exists() or get_user_model().objects.filter(username__iexact=username).exists()):
        is_taken = True
    
    data = {
        'is_taken': is_taken
    }
    return JsonResponse(data)
