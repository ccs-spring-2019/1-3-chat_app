from django.db import models
from django.urls import reverse


class Chat(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text[:50]  # it's best practice to add str() methods to all of your models

    def get_absolute_url(self):                             # docs recommend id with get_absolute_url
        return reverse('chat_detail', args=[str(self.id)])  # reverse lets us reference an object by a URL template name


