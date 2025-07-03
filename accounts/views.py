from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.shortcuts import get_object_or_404 # Import get_object_or_404
from . import forms
from posts.models import Post # To fetch user's posts

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login") # Corrected to use app_name
    template_name = "accounts/signup.html"

class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/user_profile.html'
    context_object_name = 'profile_user' # To avoid conflict with 'user' from request context

    def get_object(self, queryset=None):
        # Use username from URL to fetch the user
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.get_object()
        # Get all posts by this user
        context['user_posts'] = Post.objects.filter(user=profile_user).select_related('group').order_by('-created_at')
        # Get astrophotos specifically for a gallery section
        context['astrophotos'] = Post.objects.filter(user=profile_user, post_type='astrophoto', image__isnull=False).order_by('-created_at')
        # Potentially add other stats:
        context['post_count'] = context['user_posts'].count()
        context['group_count'] = profile_user.user_groups.count() # Assuming related_name 'user_groups' on GroupMember model
        return context
