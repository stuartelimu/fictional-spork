from django.contrib.auth import get_user_model
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.shortcuts import render
from .forms import CustomUserCreationForm, ProfileForm


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
# 0750 549 455
    def form_valid(self, form):
        form.save()
        my_form = ProfileForm(self.request.POST)
        if my_form.is_valid():
            form.instance.profile.telephone = my_form.cleaned_data.get('telephone')
        return super().form_valid(form)

# def register(request):
#     if request.method == 'POST':
#         user_form = CustomUserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             redirect('home')
#     else: 
#         return render(request, 'accounts/signup.html', {'user_form':user_form, 'profile_form':profile_form })



def validate_username(request):
    username = request.GET.get('username', None)
    is_taken = False
    if(get_user_model().objects.filter(email__iexact=username).exists() or get_user_model().objects.filter(username__iexact=username).exists()):
        is_taken = True
    
    data = {
        'is_taken': is_taken
    }
    return JsonResponse(data)
