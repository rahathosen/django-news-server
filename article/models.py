from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from reporter.models import Reporter
from categories.models import PostsTag

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


# Article section
class ArticleCategory(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Category name in English without Space and comma')
    name = models.CharField(max_length=200,  blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Category/',max_length=500)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    serial = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    total_view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'Article/Category/', output.getvalue(), None)
        super(ArticleCategory, self).save(*args, **kwargs)
        # for url
        if not self.url:
            self.url = self.uniqueId
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)

class ArticleWritter(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Writter name in English without Space and comma')
    name = models.CharField(max_length=200,  blank=True, null=True)
    Image = models.ImageField(blank=True, null=True, upload_to='Article/Writer/',max_length=500)
    details = RichTextField(blank=True, null=True)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    total_view = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):        
        if self.Image:
            img = Image.open(self.Image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.Image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.Image.name.split('.')[0], 'Article/Writer/', output.getvalue(), None)
        super(ArticleWritter, self).save(*args, **kwargs)
        # for url
        if not self.url:
            self.url = self.uniqueId
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    uniqueId = models.CharField(unique= True, max_length=100,  blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, blank=False, null=False)
    writter = models.ForeignKey(ArticleWritter, on_delete=models.DO_NOTHING, blank=False, null=False)
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING, blank=False, null=False)
    title = models.CharField(max_length=200,  blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null= True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Images',max_length=500)
    tag = models.ManyToManyField(PostsTag, blank=True)
    related_article = models.ManyToManyField('self', blank=True)
    status = models.IntegerField(choices=STATUS, default = 1)
    editor_reviewed = models.IntegerField(choices=YESNO, default = 1)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.image.url == "" or self.image.url == None or self.image.url == " ":
            if self.image:
                img = Image.open(self.image)
                output = BytesIO()
                img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
                self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'Article/images/webp', output.getvalue(), None)
            super(Article, self).save(*args, **kwargs)
        
        if self.uniqueId == " " or self.uniqueId == "" or self.uniqueId is None:
            self.uniqueId = f"{self.category.uniqueId+self.writter.uniqueId+'-'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))}"
            super().save(*args, **kwargs)
        # for url
        if not self.url:
            self.url = self.category.uniqueId + self.writter.uniqueId + self.uniqueId
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title + ' - ' + str(self.category.name) + ' - ' + str(self.writter.name)


