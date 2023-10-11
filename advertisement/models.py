from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# from webInfo.models import STATUS, YESNO 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)

#Advertisement section
class AdBox(models.Model):
    position =  models.CharField(max_length=50, blank=True, null=True)
    size =  models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField(choices=YESNO, default = 0)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Advertisement Boxes'
        verbose_name = 'Advertisement Box'

    def __str__(self):
        return self.position + " - " + self.size
    
    def save(self, *args, **kwargs):
        self.total_view = self.total_view + 1
        super().save(*args, **kwargs)
    

class AdCompany(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/company/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True)
    payment_due = models.IntegerField(choices=YESNO, default = 1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Advertisement Companies'
        verbose_name = 'Advertisement Company'

    def __str__(self):
        return self.name 


class Advertisement(models.Model):
    add_company = models.ForeignKey(AdCompany, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/Adds/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True)
    embed_code = models.TextField(blank=True, null=True)
    addBox = models.ForeignKey(AdBox, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)
    stop_at = models.DateTimeField(blank=False, null=False)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'

    def __str__(self):
                return self.title + " - " + str(self.add_company) + " - " + str(self.addBox)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'Advertisement/Adds/', output.getvalue(), None)
        super(Advertisement, self).save(*args, **kwargs)
    # for url
        if not self.url:
            slug_str = f"{self.title}"
            self.url = self.title.replace(" ", "-").replace(",", "")
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)
        
