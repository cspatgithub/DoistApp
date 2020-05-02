from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from datetime import datetime


class Task(models.Model):
    name =  models.CharField(default='Task Name', max_length=100)
    details = RichTextField()
    start_date = models.DateField(default=datetime.today)
    end_date = models.DateField()
    start_time = models.TimeField(default=datetime.now)
    end_time = models.TimeField()

    COMPLETED = (('Completed', 'Completed'), ('Uncompleted', 'Uncompleted'))
    status = models.CharField(choices=COMPLETED, default='Uncompleted', max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    of = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Task, self).save(*args, **kwargs)
    
