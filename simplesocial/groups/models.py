from django.db import models
from django.urls import reverse

# "slugify" converts any string into a URL type string
from django.utils.text import slugify

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
# helps us to create custom template tags
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(default='', blank=True)
    description_html = models.TextField(default='', blank=True, editable=False)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        # to order in ascending order of "name" data-member
        ordering = ['name']
    


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')