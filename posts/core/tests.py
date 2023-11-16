from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Test Title', description='Test Description')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        self.assertEqual(expected_object_title, 'Test Title')

    def test_description_content(self):
        post = Post.objects.get(id=1)
        expected_object_description = f'{post.description}'
        self.assertEqual(expected_object_description, 'Test Description')

    # Add more test methods as needed to cover various aspects of your model
