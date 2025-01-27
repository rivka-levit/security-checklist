from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, View

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from secure_app.forms import CreateUserForm


class IndexView(TemplateView):
    """Home page view."""

    template_name = 'secure_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SecureX'
        return context


class RegisterView(View):
    """User registration page view."""

    def get(self, request):  # noqa
        form = CreateUserForm()
        context = {
            'title': 'SecureX | Register',
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

    login_url = 'login'
    template_name = 'secure_app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SecureX | Dashboard'
        return context
