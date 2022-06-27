from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse_lazy
from blog.models import UserProfile
from users.forms import EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView, CreateView
from blog.forms import UserProfileForm


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/change-password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'users/password_success.html')


class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        
        return context

class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'users/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'linkedin_url', 'github_url']
    success_url = reverse_lazy('showprofile')


class CreateProfilePageView(CreateView):
    form_class = UserProfileForm
    template_name = 'users/create_profile_page.html'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('index')