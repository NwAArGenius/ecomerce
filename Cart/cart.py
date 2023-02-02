
from decimal import Decimal
from Shop.models import Product
from django.conf import settings


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

        # methode pour ajouter des itmes au cart
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 1, "price": str(product.price)}
            if override_quantity:
                self.cart[product_id]["quantity"] = quantity
            else:
                self.cart[product_id]["quantity"] += quantity
            self.save()

            # methode permetant de suppimer un item dans le cart

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

            # recuperer tous les elemment du panier
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        # compter les element dans le panier

    def __len__(self):

        return sum(item['quantity'] for item in self.cart.values())
        # calculer la valeur total du panier

    def get_total_price(self):
        return sum(Decimal(item['price']*item['quantity']
                           for item in self.cart.values()))

        # vider le panier
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
