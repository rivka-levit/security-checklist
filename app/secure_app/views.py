from django.shortcuts import render

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Secure Checklist'
        return context


class RegisterView(View):
    def get(self, request):
        context = {'title': 'Secure Checklist | Register'}
        return render(request, 'register.html', context)


class LoginView(View):
    def get(self, request):
        context = {'title': 'Secure Checklist | Login'}
        return render(request, 'login.html', context)


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Secure Checklist | Dashboard'
        return context
