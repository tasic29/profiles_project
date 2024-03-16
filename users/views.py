from django.shortcuts import render
from django.views.generic import CreateView, View
from django.urls import reverse_lazy

from users.models import MyUser
from .forms import MyUserCreationForm


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('thank-you')


def thank_you(request):
    return render(request, 'thank_you.html')
