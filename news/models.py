from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils.text import slugify
import random
import string
from reporter.models import Reporter
from categories.models import *

from datetime import *
from django.utils import timezone

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
YESNO = (
    (0, "No"),
    (1, "Yes")
)

class Post(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name= 'This unique Id will be auto generate')
    reported_by = models.ForeignKey(Reporter, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Reporter')
    category = models.ForeignKey(NewsCategory, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Category')
    subcategory = models.ForeignKey(NewsSubCategory, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Sub Category')
    continent = models.ForeignKey(Continent, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Continent')
    country = models.ForeignKey(Country, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Country')
    division = models.ForeignKey(Division, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Division')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='District')
    city_corporation = models.ForeignKey(CityCorporation, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='City Corporation')
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Upozila')
    pourosava = models.ForeignKey(Pourosava, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Pourosava')
    thana = models.ForeignKey(Thana, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Thana')
    union = models.ForeignKey(Union, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Union')
    zip_code = models.ForeignKey(ZipPostalCode, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Zip Code')
    turisum_spot = models.ForeignKey(TurisumSpot, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Tourism Spot')
    title = models.CharField(max_length=200, blank=False, verbose_name='Title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    details = RichTextField(blank=True, null=True, verbose_name='Details')
    related_post = models.ManyToManyField('self', blank=True, verbose_name='Related Post Suggestion')
    image = models.ImageField(blank=True, null=True, verbose_name='Image')
    image_source = models.CharField(max_length=100, blank=True, null=True, verbose_name='Image Source')
    video_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='Video Link')
    video_source = models.CharField(max_length=100, blank=True, null=True, verbose_name='Video Source')
    tag = models.ManyToManyField(PostsTag, blank=True, verbose_name='Tags')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=False, editable=True, verbose_name='Updated At')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='Status')
    editor_reviewed = models.IntegerField(choices=YESNO, default=0, verbose_name='Editor Review')
    is_highlight_on_section = models.IntegerField(choices=YESNO, default=0, verbose_name='Highlight on section')
    total_view = models.PositiveIntegerField(default=0, verbose_name='Total View (*Do not edit)')

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Post'
        verbose_name_plural = 'All Posts'

    def __str__(self):
        return f"{self.title} - {self.category.title} - {self.subcategory.title}"
        
    def save(self, *args, **kwargs):
        if not self.uniqueId or not self.uniqueId.strip():
            uid = f"{self.country.uniqueId}{self.category.uniqueId}{self.subcategory.uniqueId}{''.join(random.choice(string.digits) for _ in range(6))}"
            self.uniqueId = slugify(uid).replace("-", "")
        super(Post, self).save(*args, **kwargs)
        original_title = Post.objects.filter(pk=self.pk).values_list('title', flat=True)
        original_details = Post.objects.filter(pk=self.pk).values_list('details', flat=True)
        original_description = Post.objects.filter(pk=self.pk).values_list('description', flat=True)

        if self.pk and (self.title != original_title[0] or self.details != original_details[0] or self.description != original_description[0]):
            self.updated_at = timezone.now()
        super(Post, self).save(*args, **kwargs)
