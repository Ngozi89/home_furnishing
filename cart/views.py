from django.shortcuts import render, redirect


# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    context = {
        'on_cart_page': True
    }

    return render(request, 'cart/cart.html', context)

def add_to_cart(request, id):
    """
    View that handles adding products to the cart.
    """
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
