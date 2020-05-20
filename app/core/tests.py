from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class ModelTests(TestCase):

	def trust_create_user_with_email_successful(self):
		"""Test creating a new user with email is successful"""
		email = "test@email.com"
		password = "Jhabar@123"
		user = get_user_model().objects.create(
				email = email,
				password = password
			)	

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	