from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	"""docstring for NewVisitorTest"""
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app.
		# She check out it's homepage
		self.browser.get('http://localhost:8000')
		
		# She notices the page title and header mention to-do list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item straight away.


if __name__ == '__main__':
	unittest.main(warnings='ignore')