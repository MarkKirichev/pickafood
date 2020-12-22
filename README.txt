# Pickafood

Pickafood is a Python project for food deliverings and a system for making orders to local restaurants.
Users and Admins have full CRUD. 
Admin profiles are recognized when during registration emails have a certain restaurant's slug pattern in their regex expressions.
Users can order items from the restaurants.
Admins can receive and manage orders from their profile pages.

- Form validation is added
- CSS/Bootstrap/JS files are found in the static folder
- Class-based views are implemented, as can be seen in the pickafood/urls.py file
- Additional implementations:
	- template tags
	- forgotten password -> changing password through email
	- additional functionality file with further validations for JS queries
	- AJAX
	- jQuery
	- signals for one-to-one relationship between Django's user and Profile items
	- custom ListField for storing Lists into the database as classes
	- hashing username & password before sending in to the database
	- context processors: all project html templates can access the Restaurant context 

## Installation

Download the Pickafood project from this Github account and install all the needed packages described in the requirements file.

## Usage

```python
# if there are any new migrations
python manage.py makemigrations 
# if you don't want to run the server on the default port
python manage.py runserver 8080 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
No license yet.