from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()
class TestBase(TestCase):
    PET_DATA = {
        "name": "TestPet",
        "pet_photo": "https://example.com/test.jpg",
        "date_of_birth": "2020-01-01",

    }

    USER_DATA = {
        "email": "TestUser@softuni.bg",
        "password": "TestPassword"
    }

    def _create_user(self):
        return UserModel.objects.create_user(**self.USER_DATA)