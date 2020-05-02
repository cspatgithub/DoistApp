from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


class Note(models.Model):
    title = models.CharField(default='', max_length=120)
    text = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)

    of = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Note, self).save(*args, **kwargs)
