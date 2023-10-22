from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import random
import string

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Advertisement section
class AdBox(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Unique Id will be generated automatically')
    position =  models.CharField(max_length=50, blank=True, null=True)
    size =  models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField(choices=YESNO, default = 0)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Advertisement Boxes'
        verbose_name = 'Advertisement Box'

    def __str__(self):
        return self.position + " - " + self.size

class AdCompany(models.Model):
    uniqueId = models.CharField(unique=True, default= randomString, max_length=20, blank=False, null=False, verbose_name='Unique Id will be generated automatically')
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/company/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Company Link')
    payment_due = models.IntegerField(choices=YESNO, default = 1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Advertisement Companies'
        verbose_name = 'Advertisement Company'

    def __str__(self):
        return self.name 


class Advertisement(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Unique Id will be generated automatically')
    add_company = models.ForeignKey(AdCompany, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/Adds/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True)
    embed_code = models.TextField(blank=True, null=True)
    addBox = models.ForeignKey(AdBox, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)
    stop_at = models.DateTimeField(blank=False, null=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'

    def __str__(self):
                return self.title + " - " + str(self.add_company) + " - " + str(self.addBox)

    def save(self, *args, **kwargs):
        if self.image.url != self.image.field.path:
            if self.image:
                img = Image.open(self.image)
                output = BytesIO()
                img = img.convert('RGB')
                img.save(output, format='WEBP', quality=95, subsampling=0)
                output.seek(0)
                self.image = InMemoryUploadedFile(output, 'ImageField', f"{self.image.name.split('.')[0]}.webp", 'Article/images/webp', output.read(), None)
            super().save(*args, **kwargs)

        if self.uniqueId == " " or self.uniqueId == "" or self.uniqueId is None:
            self.uniqueId = self.add_company.name + str(self.addBox.position) + str(self.addBox.size) + ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            super(Advertisement, self).save(*args, **kwargs)
    
        
