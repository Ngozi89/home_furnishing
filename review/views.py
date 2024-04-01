from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from products.models import Product

from .forms import ReviewForm


@login_required
def create_review(request, product_id):
    """
    View to create a review on a product page.
    """
    products = Product.objects.get(id=product_id)
    user = request.user
    user_profile = user.userprofile

    # checking if the user has any orders, because
    # if they don't then there is no point continuing
    if not user_profile.orders.all():
        messages.error(
            request, "You must have purchased this product to review it.")
        return redirect('product_detail', product_id)

    # check if the user has orders and the product is in
    # one of the orders, if not then the user can't review
    orders = user_profile.orders.all()
    product_purchased = False

    for order in orders:
        for item in order.line_items.all():
            if item.product == product:
                product_purchased = True
                break
        if product_purchased:
            break

    if not product_purchased:
        messages.error(
            request, "You must have purchased this product to review it.")
        return redirect('product_detail', product_id)

    # check if the user has already reviewed the product
    review_exists = Review.objects.filter(product=product, user=user).exists()

    if review_exists:
        messages.error(
            request, "You have already reviewed this product, "
            "please update or delete your existing review.")
        return redirect('product_detail', product_id)

    form = ReviewForm()

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review(
            product=product,
            user=user,
            title=title,
            text=text,
            rating=rating
        )
        review.save()

        messages.success(request, "Your review has been added.")
        return redirect('product_detail', product_id)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'review/create_review.html', context)


@login_required
def edit_review(request, review_id):
    """
    View to edit a review.
    """
    review = Review.objects.get(id=review_id)
    product = review.product
    form = ReviewForm(initial={
        'title': review.title,
        'text': review.text,
        'rating': review.rating
    })

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review.title = title
        review.text = text
        review.rating = rating
        review.save()

        messages.success(request, "Your review has been updated.")
        return redirect('product_detail', product.id)

    context = {
        'product': product,
        'form': form,
        'review': review,
    }

    return render(request, 'review/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    View to delete a review.
    """
    review = Review.objects.get(id=review_id)
    products = review.product
    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('product_detail', product.id)


@login_required
def helpful_votes(request, review_id):
    """
    View to toggle helpful votes on a review.
    """
    review = Review.objects.get(id=review_id)
    user = request.user

    if not user.is_authenticated:
        messages.error(request, "You must be logged in to upvote.")
        return redirect('product_detail', review.product.id)

    if user in review.helpful_votes.all():
        review.helpful_votes.remove(user)
        messages.success(request, "You have removed your upvote.")
    else:
        review.helpful_votes.add(user)
        messages.success(request, "You have added your upvote.")

    return redirect('product_detail', review.product.id)