from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OP1ZdLdrv5Glop8ovoWd3K50cUhMrOY5zJirOyxz9NwTzb3u9uolW4Y0BAWdRSBzyTs7zIqbPI3n4FhvuZy1wIY00xeosuhJK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
