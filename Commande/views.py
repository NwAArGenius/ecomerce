from django.shortcuts import render, HttpResponse
from .forms import OrderCreateForm
from Cart.cart import Cart
from .models import OrderItem
# Create your views here.


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
                cart.clear()
                request.session["order_id"] = order.id
                return HttpResponse("<h2> votre commande est valider</h2>")
    else:
        form = OrderCreateForm
        return render(request, 'orders/create.html', {'cart': cart,
                                                      'form': form})
