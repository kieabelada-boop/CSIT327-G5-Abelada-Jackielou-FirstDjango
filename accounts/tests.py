from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class AccountFlowTests(TestCase):
	def test_signup_shows_success_message(self):
		response = self.client.post(reverse("signup"), {
			"username": "newstudent",
			"email": "student@example.com",
			"first_name": "New",
			"last_name": "Student",
			"course": "Science",
			"password1": "Test-password-482!",
			"password2": "Test-password-482!",
		}, follow=True)

		self.assertContains(response, "Your account has been created")
		self.assertTemplateUsed(response, "registration/login.html")

	def test_profile_update_changes_only_signed_in_user(self):
		user = CustomUser.objects.create_user(
			username="student", password="Test-password-482!", course="Science"
		)
		other_user = CustomUser.objects.create_user(
			username="other", password="Test-password-482!", course="History"
		)
		self.client.force_login(user)

		response = self.client.get(reverse("profile"))
		self.assertTemplateUsed(response, "registration/profile.html")

		response = self.client.post(reverse("profile"), {
			"username": "student",
			"email": "student@example.com",
			"first_name": "Updated",
			"last_name": "Student",
			"course": "Mathematics",
		})

		self.assertRedirects(response, reverse("dashboard"))
		user.refresh_from_db()
		other_user.refresh_from_db()
		self.assertEqual(user.course, "Mathematics")
		self.assertEqual(user.first_name, "Updated")
		self.assertEqual(other_user.course, "History")

	def test_profile_requires_authentication(self):
		response = self.client.get(reverse("profile"))

		self.assertRedirects(response, f"{reverse('login')}?next={reverse('profile')}")
