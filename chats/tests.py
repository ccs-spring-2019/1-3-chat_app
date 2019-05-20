from django.contrib.auth import get_user_model
from django.test import TestCase  # TestCase lets us create a sample database
from django.urls import reverse

from .models import Chat


class ChatModelTest(TestCase):

    def setUp(self):
        Chat.objects.create(text='sample chat message')

    def test_text_content(self):
        chat = Chat.objects.get(id=1)
        expected_object_name = f'{chat.text}'  # f strings let us put variables directly in our strings
        self.assertEqual(expected_object_name, 'sample chat message')


class HomePageViewTest(TestCase):

    def setUp(self):
        Chat.objects.create(text='sample chat message')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))  # reverse('home') generates URL from View name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class ChatTests(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='safepass'
        )

        self.chat = Chat.objects.create(
            title='A good title',
            text='This is a really good chat message',
            author=self.user
        )

    # def test_string_representation(self):
    #     chat = Chat(title='A new title')
    #     self.assertEqual(str(chat), chat.title)

    def test_chat_content(self):
        self.assertEqual(f'{self.chat.title}', 'A good title')
        self.assertEqual(f'{self.chat.author}', 'testuser')
        self.assertEqual(f'{self.chat.text}', 'This is a really good chat message')

    def test_chat_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'This is a really good chat message')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/chat/1/')
        no_response = self.client.get('/chat/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'chat_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.chat.get_absolute_url(), '/chat/1/')

    def test_chat_create_view(self):
        response = self.client.get(reverse('chat_new'), {
            'title': 'A new title',
            'text': 'Read my awesome chat message',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'A new title')
        # self.assertContains(response, 'Read my awesome chat message')

    # def test_chat_update_view(self):
    #     response = self.client.get(reverse('chat_edit', args='1'), {
    #         'title': 'Updated chat title',
    #         'text': 'Updated chat text',
    #     })
    #     self.assertEqual(response.status_code, 302)

    def test_chat_delete_view(self):
        response = self.client.get(
            reverse('chat_delete', args='1'))
        self.assertEqual(response.status_code, 200)
