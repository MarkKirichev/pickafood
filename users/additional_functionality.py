from app.models import OrderItem


def get_restaurant_name(original_restaurant_name: str):
    email_restaurant_name = ''

    for char in original_restaurant_name:
        if not char == ' ':
            email_restaurant_name += char

    return email_restaurant_name.lower()


def check_for_everything(json_dict: dict):
    list_items_that_should_be_in_order_dict = [
        'date',
        'time',
        'peopleNumber',
        'names',
        'phoneInput',
        'emailInput',
        'cart'
    ]

    counter = 0
    for item in list_items_that_should_be_in_order_dict:
        if item in json_dict.keys() and (not json_dict[item] is None):
            counter += 1

    if ('restaurant' in json_dict['cart']
        and (not json_dict['cart']['restaurant'] is None)):
        counter += 1

    if len(json_dict['cart']['items']) > 0:
        if counter == (len(list_items_that_should_be_in_order_dict) + 1):
            return True

    return False
