from django.shortcuts import render, redirect

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from secure_app.forms import CreateUserForm


class IndexView(TemplateView):
    template_name = 'secure_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SecureX'
        return context


class RegisterView(View):
    def get(self, request):
        form = CreateUserForm()
        context = {
            'title': 'SecureX | Register',
            'register_form': form,
        }
        return render(request, 'secure_app/register.html', context)

    def post(self, request):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        return redirect(request.META.get('HTTP_REFERER'))


class LoginView(View):
    def get(self, request):
        context = {'title': 'SecureX | Login'}
        return render(request, 'secure_app/login.html', context)


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'secure_app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SecureX | Dashboard'
        return context
