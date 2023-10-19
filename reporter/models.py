from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Reporter(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=40,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='Reporter/',blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Reporters/Stuffs'
        verbose_name = 'Reporter/Stuff'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'Reporter/', output.getvalue(), None)
        super(Reporter, self).save(*args, **kwargs)