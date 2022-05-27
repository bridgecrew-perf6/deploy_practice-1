from django.db import models
from django.urls import reverse

import misaka

# for connecting a post to a Group
from groups.models import Group

# for connecting the "post" to the USER who is currently LOGGED IN
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={"username": self.user.username, "pk": self.pk})

    class Meta:
        # to order in descending order of "created_at" data-member
        ordering = ['-created_at']
        unique_together = ['user', 'message']