from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page
from django.template.loader import render_to_string # render the template in test
from lists.models import Item

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	
	def test_home_page_returns_correct_html(self):
		# Before 
		# response = home_page(request)
		
		# Now
		# [self.client.get('/')] checks which template is used for root 
		# Instead of manually creating an HttpRequest object and calling the view
		# function directly, we call self.client.get , passing it the URL we want
		# to test
		response = self.client.get('/')

		# Use [request = HttpRequest()] only if [response = home_page(request)] is used
		# request = HttpRequest()
		# docode is also not import if we use client.get method. So lets comment out this line
		# html = response.content.decode('utf-8')
		
		# Use these three lines of code that given below. Finally we are not going to 
		# use these three lines of code. So we comment out 
		# [start]
		# self.assertTrue(html.strip().startswith('<html>'))
		# self.assertIn('<title>To-Do lists</title>', html)
		# self.assertTrue(html.strip().endswith('</html>'))
		# [end]
		
		# or use next two lines of code [start]
		# expected_html = render_to_string('home.html')
		# self.assertEqual(html, expected_html)
		# [end]
		
		# [ assertTemplateUsed ] is the test method that the django TestCase class
		# provides us. It lets us check what template was used to render a response
		# (NB - it will only work for responses that were retrieved by the Test Client.)
		self.assertTemplateUsed(response, 'home.html')
	

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	def test_can_save_a_post_request(self):
		response = self.client.post('/', data={'item_text':'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')

