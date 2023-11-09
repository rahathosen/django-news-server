from django.db import models
from django.utils.text import slugify
from PIL import Image
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


#Advertisement section
class AdBox(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Unique Id')
    position =  models.CharField(max_length=50, blank=False, null=False)
    size =  models.CharField(max_length=50, blank=False, null=False)
    active = models.IntegerField(choices=YESNO, default = 0)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["total_view"]
        verbose_name_plural = 'Advertisement Boxes'
        verbose_name = 'Advertisement Box'
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(AdBox, self).save(*args, **kwargs)

    def __str__(self):
        return self.position + " - " + self.size


class AdCompany(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Unique Id ')
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name='Company Name')
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/company/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Company Link')
    payment_due = models.IntegerField(choices=YESNO, default = 1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Advertisement Companies'
        verbose_name = 'Advertisement Company'
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(AdCompany, self).save(*args, **kwargs)

    def __str__(self):
        return self.name 


class Advertisement(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name='Unique Id will be generated automatically')
    add_company = models.ForeignKey(AdCompany, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(blank=True, null=True, upload_to='Advertisement/Adds/',max_length=500)
    link = models.CharField(max_length=200, blank=True, null=True)
    embed_code = models.TextField(blank=True, null=True)
    addBox = models.ForeignKey(AdBox, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    stop_at = models.DateTimeField(blank=False, null=False)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'

    def __str__(self):
                return self.title + " - " + str(self.add_company) + " - " + str(self.addBox)

    def save(self, *args, **kwargs):
        if not self.uniqueId or not self.uniqueId.strip():
            uid = f"{self.addBox.uniqueId}{self.add_company.uniqueId}{''.join(random.choice(string.digits) for _ in range(2))}"
            self.uniqueId = slugify(uid).replace("-", "")
        super(Advertisement, self).save(*args, **kwargs)
    
        
