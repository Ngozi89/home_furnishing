from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product


# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """
    View that handles adding products to the cart.
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity


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
    else:
        cart.pop(item_id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_item_from_cart(request, item_id):
    """
    Removes the item from the shopping cart
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart

        return redirect(reverse('view_cart'))

    except Exception as e:
        return HttpResponse(status=500)