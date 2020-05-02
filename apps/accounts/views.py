from django.shortcuts import render
from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.urls import reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Profile
from .forms import SignUpForm


def SignUpView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.email = form.cleaned_data.get('email')
        user.profile.slug = form.cleaned_data.get('username')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('profile-detail', kwargs={'slug':username}))
    else:
        form =SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    fields = [
        'name',
        'email',
        'phone_number',
        'location',
        'gender'
    ]
    template_name = 'accounts/profile_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'slug': self.request.user.username})
