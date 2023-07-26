import stripe
from django.core.management import call_command


def create_product(new_payment_product):
    product = stripe.Product.create(name=f"{new_payment_product}")
    return product


def create_price(new_payment, product):
    price = stripe.Price.create(
        unit_amount=new_payment.payment_sum,
        currency="rub",
        recurring={"interval": "month"},
        product=f"{product['id']}",
    )
    return price


def create_payment(price):
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


def get_payment_status(payment_id):
    payment_info = stripe.checkout.Session.retrieve(
        f"{payment_id}",
    )
    return payment_info['payment_status'] == 'paid'

def set_pay_status(payment_object):
    if get_payment_status(payment_object.payment_id):
        payment_object.is_paid = True
        call_command('remove_payment_tracking', f'{payment_object.pk}')
