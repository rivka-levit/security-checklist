from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(View):
    pass


class LoginView(View):
    pass


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'dashboard.html'
