from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import RegisterForm
from django.contrib.auth.models import User


class SignUp(FormView):
    """ Views for registering user """

    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/user/all_user/'

    def form_valid(self, form):
        print(form.cleaned_data)
        if super().form_valid(form):
            form.save(commit=True)
            return super().form_valid(form)
        return super().form_valid(form)


class AppUsers(ListView):
    """List view of users"""

    model = User
