def get_restaurant_name(original_restaurant_name: str):
    email_restaurant_name = ''

    for char in original_restaurant_name:
        if not char == ' ':
            email_restaurant_name += char

    return email_restaurant_name.lower()