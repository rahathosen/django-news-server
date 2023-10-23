from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image

class Reporter(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name= 'Reporter name in English without Space and comma')
    name = models.CharField(max_length=100,blank=False, null=False)
    designation = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=40,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(default="", blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Reporters/Stuffs'
        verbose_name = 'Reporter/Stuff'

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Reporter, self).save(*args, **kwargs)