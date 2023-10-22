from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils.text import slugify
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from reporter.models import Reporter
from categories.models import PostsTag

import random
import string

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
YESNO = (
    (0, "No"),
    (1, "Yes")
)


# Article section
class ArticleCategory(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Category name in English without Space and comma')
    name = models.CharField(max_length=100, blank=False, null=False)
    details = models.TextField(default="", blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Category/', max_length=500)
    serial = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Article Categories'
        verbose_name = 'Article Category'

    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(ArticleWritter, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class ArticleWritter(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Writer name in English without Space and comma')
    name = models.CharField(max_length=100, blank= False, null=False)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Writer/', max_length=500)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
       verbose_name_plural = 'Article Writters'
       verbose_name = 'Article Writter'

    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(ArticleWritter, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name='Unique Id will be generated automatically')
    category = models.ForeignKey(ArticleCategory, to_field= 'uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='article_category')
    writter = models.ForeignKey(ArticleWritter, to_field= 'uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='article_writter')
    reported_by = models.ForeignKey(Reporter, to_field= 'uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='article_reporter')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(default="", blank=True, null=True, verbose_name='Image')
    image_source = models.CharField(max_length=100, blank=True, null=True)
    tag = models.ManyToManyField(PostsTag, blank=True)
    related_article = models.ManyToManyField('self', blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    editor_reviewed = models.IntegerField(choices=YESNO, default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Articles'
        verbose_name = 'Article'

    def save(self, *args, **kwargs):
        if not self.uniqueId:
            uId = f"{self.category.uniqueId}{self.writter.uniqueId}{''.join(random.choice(string.ascii_letters) for _ in range(4))}"
            self.uniqueId = slugify(uId).replace("-", "")
            super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.category.name} - {self.writter.name}"
