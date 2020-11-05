from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='arena_pics')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='menu_media')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        """Return a string representation of the model"""
        if self.text > self.text[:50]:
            return f"{self.text[:50]} ..."
        else:
            return self.text




    