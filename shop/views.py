from django.shortcuts import render, redirect, reverse
from .forms import UserRegistrerForm, OrderForm, ProviderCreationForm
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Provider, Offer, User
from django.core.mail import send_mail

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


class ProvidersView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'coffeshop/providers.html'
    paginate_by = 5
    context_object_name = 'providers'
    ordering = ['name']


class OffersView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'coffeshop/offers.html'
    paginate_by = 5
    context_object_name = 'offers'
    ordering = ['name']


class ProviderDetailView(LoginRequiredMixin, View):
    def get(self, request, provider):
        offers = Provider.objects.get(id=provider).offer_set.all()
        return render(request, 'coffeshop/offers.html', {'offers':offers})


class OfferDetailView(LoginRequiredMixin, View):
    def get(self, request, offer_id):
        form = OrderForm()
        order = Offer.objects.get(id=offer_id)
        return render(request, 'coffeshop/offer-detail.html',{'form':form,
                                                              'order':order})
    def post(self, request, offer_id):
        form = OrderForm(request.POST)
        order = Offer.objects.get(id=offer_id)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            street = form.cleaned_data.get('street')
            house_number = form.cleaned_data.get('house_number')
            size = form.cleaned_data.get('size')
            user_id = self.request.user.id
            user_name = self.request.user.first_name
            user_surname = self.request.user.last_name

            message = f'New coffee has been orderred:\n\n' \
                      f'Order: {order.name} {size}\n' \
                      f'Customer {user_name} {user_surname}\n' \
                      f'Address: {city}, {street}, {house_number}.'

            send_mail(f'New order: {order.name} {size}',message,'JakNowySolutions@gmail.com',{order.provider.email})
            return redirect('thanks',user_id=user_id)
        else:
            return render(request, 'coffeshop/offer-detail.html', {'form': form,
                                                                   'order': order})


class ThanksView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'coffeshop/thanks.html', {'user':user.first_name})


class ProviderCreationView(CreateView):
    model = Provider
    fields = ['name', 'email', 'image', 'address', 'description', 'phone_number']
    template_name = 'coffeshop/provider-new.html'
    # success_url = reverse('providers')
