from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Reporter(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name= 'Reporter name in English without Space and comma')
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
            if self.image.name.endswith('.webp') or self.image.url.endswith('.webp'):
                pass
            else:
                img = Image.open(self.image)
                output = BytesIO()
                img = img.convert('RGB')
                img.save(output, format='WEBP', quality=95, subsampling=0)
                output.seek(0)
                self.image = InMemoryUploadedFile(output, 'ImageField', f"{self.image.name.split('.')[0]}.webp", 'images/webp', output.read(), None)
                super().save(*args, **kwargs)

        if self.uniqueId != " " or self.uniqueId != "" or self.uniqueId is not None:
            self.uniqueId = self.uniqueId.replace(" ", "-")
            super(Reporter, self).save(*args, **kwargs)