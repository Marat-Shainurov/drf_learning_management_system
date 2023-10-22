import stripe
from django.conf import settings

from courses.models import Payment


def create_product(new_payment_product: str) -> dict:
    """Creates a new product for a stripe session (payment)"""
    product = stripe.Product.create(name=new_payment_product)
    return product


def create_price(new_payment: Payment, product: dict) -> dict:
    """Creates a new price for an existing product and a stripe session (payment)."""
    price = stripe.Price.create(
        unit_amount=new_payment.payment_sum,
        currency="rub",
        recurring={"interval": "month"},
        product=f"{product['id']}",
    )
    return price


def create_payment(price: dict) -> dict:
    """Creates a new stripe session (stripe payment)."""
    payment = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": f"{price['id']}",
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return payment


def get_payment_status(payment_id: str) -> bool:
    """Checks whether a payment has been made or not."""
    stripe.api_key = settings.STRIPE_API_KEY
    payment_info = stripe.checkout.Session.retrieve(payment_id)
    return payment_info['payment_status'] == 'paid'
