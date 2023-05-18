from django.test import TestCase

# Create your tests here.
cart = {
    '1': {
        'id': 1,
        'name': 'IBANEZ V50NJP ACOUSTIC GUITAR',
        'qty': 4
    },
    '3': {
        'id': 1,
        'name': 'IBANEZ V50NJP ACOUSTIC GUITAR',
        'qty': 4
    },
    '2': {
        'id': 1,
        'name': 'IBANEZ V50NJP ACOUSTIC GUITAR',
        'qty': 4
    }
}

for item, item_data in cart.items():
    print(f"Product ID: {item_data['id']}")
    print(f"Product Name: {item_data['name']}")
    print(f"Quantity: {item_data['qty']}")
