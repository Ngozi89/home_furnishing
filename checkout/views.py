from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OP1ZdLdrv5Glop8ovoWd3K50cUhMrOY5zJirOyxz9NwTzb3u9uolW4Y0BAWdRSBzyTs7zIqbPI3n4FhvuZy1wIY00xeosuhJK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
