from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, View, RedirectView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth

from secure_app.forms import CreateUserForm


class IndexView(TemplateView):
    """Home page view."""

    template_name = 'secure_app/index.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(*args, **kwargs)


class RegisterView(View):
    """User registration page view."""

    def get(self, request):  # noqa
        form = CreateUserForm()
        context = {
            'register_form': form,
        }
        return render(request, 'secure_app/register.html', context)

    def post(self, request):  # noqa
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Account was created successfully!')
            return redirect('two_factor:login')

        messages.error(request, 'Invalid data provided.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DashboardView(LoginRequiredMixin, TemplateView):
    """User dashboard page view."""

    login_url = 'two_factor:login'
    template_name = 'secure_app/dashboard.html'


def user_logout(request):
    """User logout."""

    auth.logout(request)
    return redirect('index')
