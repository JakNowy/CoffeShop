from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegistrerForm
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Provider, Offer

class RegisterView(View):
    def get(self, request):
        form = UserRegistrerForm()
        return render(request, 'coffeshop/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'coffeshop/register.html', {'form': form})

class ProvidersView(ListView):
    model = Provider
    template_name = 'coffeshop/providers.html'
    paginate_by = 5
    context_object_name = 'providers'


class OffersView(ListView):
    model = Offer
    template_name = 'coffeshop/offers.html'
    paginate_by = 5
    context_object_name = 'offers'