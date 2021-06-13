from django.test import TestCase
from .forms import ContactForm
from .models import Product, Category


# Test the contact form
class TestContactForm(TestCase):

    def test_contact_form_valid_data(self):
        '''This test checks if the data returned from a filled out contact form is valid'''

        form = ContactForm(data={
            "name": "Christian",
            "email": "chrpe30@gmail.com",
            "message": "Hi there!",
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_empty_name_field(self):
        '''This test checks if it's possible to submit the form with an empty name field'''

        form = ContactForm(data={
            "name": "",
            "email": "chrpe30@gmail.com",
            "message": "Hi there!",
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


# Test the models
class TestModels(TestCase):
    '''Testing if the model is represented correctly as a string'''

    def test_category_str(self):
        category_name = Category.objects.create(category_name="Water")

        self.assertEqual(str(category_name), "Water")


class TestViews(TestCase):
    '''Testing the views'''

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/index.html")

    def test_add_cart(self):
        response = self.client.get("/add_cart")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/cart.html")

    def test_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/contact.html")

    def test_store(self):
        response = self.client.get("/store/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/store.html")

    def categories(self):
        category = Category.objects.create(category_name="some_name")
        response = self.client.get(f'/categories/{category.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/categories.html')

    def ind_products(self):
        product = Product.objects.create(product_name="some_name")
        response = self.client.get(f'/categories/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/individual_products.html')

    def remove_from_cart(self):
        response = self.client.get("/remove_from_cart/")
        self.assertRedirects(response, '/')
