from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import reverse
from PIL import Image


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'Mr/Mrs.{self.first_name} {self.last_name}'

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
        instance.customer.save()


class Provider(models.Model):
    name = models.CharField(max_length=20, verbose_name='Company name')
    description = models.TextField()
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    image = models.ImageField(default='provider.jpg', upload_to='provider-imgs')
    email = models.EmailField(max_length=50)

    def get_absolute_url(self):
        return reverse('providers')

    def __str__(self):
        return f'{self.name} \n Address: {self.address}, phone:{self.phone_number}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 50 or img.width > 50:
            output_size = (50,50)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Offer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=1)
    price_S = models.DecimalField(decimal_places=2, max_digits=5)
    price_M = models.DecimalField(decimal_places=2, max_digits=5)
    price_L = models.DecimalField(decimal_places=2, max_digits=5)
    with_sugar = models.BooleanField(default=False)
    image = models.ImageField(default='coffee.jpg', upload_to='offer-imgs')

    def __str__(self):
        return f'{self.name} coffee. {self.price_S}/{self.price_M}/{self.price_L}'