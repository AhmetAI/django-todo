from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string



# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)


    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Todo.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + "-" + get_random_string(length=10)
        super(Todo, self).save(*args, **kwargs)