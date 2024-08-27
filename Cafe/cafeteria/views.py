from django.shortcuts import render, redirect
from .models import Dish, CartItem

def Menu(request):
    dishes = Dish.objects.all()
    return render(request, 'Menu/menu.html', {'dishes': dishes})


def contact(request):
    return render(request, 'Menu/contact.html')
def about(request):
    return render(request, 'Menu/about.html')

def add_to_cart(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    cart_item, created = CartItem.objects.get_or_create(dish=dish)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'Menu/cart.html', {'cart_items': cart_items})

def update_cart(request, cart_item_id, action):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if action == 'add':
        cart_item.quantity += 1
    elif action == 'subtract':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            cart_item.delete()
            return redirect('cart')
    elif action == 'delete':
        cart_item.delete()
        return redirect('cart')
    cart_item.save()
    return redirect('cart')
