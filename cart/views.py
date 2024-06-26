from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """
    View that handles adding products to the cart.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += int(quantity)
        messages.success(request,
                         f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = int(quantity)
        messages.success(request, f'Added {product.name} to your cart')


    request.session['cart'] = cart
    print(f'cart contents : {request.session['cart']}')
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                         (f'Updated {product.name} '
                             f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request,
                         (f'Removed {product.name} '
                             f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_item_from_cart(request, item_id):
    """
    Removes the item from the shopping cart
    """
    cart = request.session.get('cart', {})
    product = get_object_or_404(Producct, pk=item_id)
    if item_id in cart.keys():
        try:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')
            request.session['cart'] = cart
            return redirect(reverse('view-cart'))
        except Exception as e:
            messages.error(request, f'An error occured {e}')
            return HttpResponse(status=500)