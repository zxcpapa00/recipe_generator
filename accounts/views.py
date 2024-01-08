from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import LoginForm, RegisterForm
from service.models import Story


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


class SignUpView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')


class StoryView(generic.ListView):
    model = Story
    template_name = 'story.html'


def set_story(user, products, response_prod):
    Story.objects.create(user=user, products=products, recipe=response_prod)
