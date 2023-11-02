from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from reporter.models import Reporter
from article.models import ArticleWritter
from categories.models import *
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

class Feature(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Name in English without Space')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Feature Title')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Feature/',blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        ordering = ["serial"]
        verbose_name_plural = 'Features'
        verbose_name = 'Feature'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Feature, self).save(*args, **kwargs)
        

class FeatureCategory(models.Model):
    uniqueId = models.CharField( unique=True, max_length=20, blank=False, null=False, verbose_name='Category Name in English without Space')
    feature = models.ForeignKey(Feature, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Feature Category Title')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Feature/',blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["serial"]
        verbose_name_plural = 'Feature Categories'
        verbose_name = 'Feature Category'

    def __str__(self):
        return self.title + self.feature.title
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(FeatureCategory, self).save(*args, **kwargs)
        

class FeaturePost(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100,  blank=True, null=True)
    feature = models.ForeignKey(Feature, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature')
    category = models.ForeignKey(FeatureCategory, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature Category')
    continent = models.ForeignKey(Continent, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Continent')
    country = models.ForeignKey(Country, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Country')
    division = models.ForeignKey(Division, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Division')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='District')
    city_corporation = models.ForeignKey(CityCorporation, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='City Corporation')
    upozila = models.ForeignKey(Upozila, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Upozila')
    pourosava = models.ForeignKey(Pourosava, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Pourosava')
    thana = models.ForeignKey(Thana, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Thana')
    union = models.ForeignKey(Union, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Union')
    zip_code = models.ForeignKey(ZipPostalCode, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null= True, verbose_name='Zip Code')
    turisum_spot = models.ForeignKey(TurisumSpot, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Turisum Spot')
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    details = RichTextField(blank=True, null=True, verbose_name='Details')
    related_post = models.ManyToManyField('self', blank=True, verbose_name='Related Post Suggation')
    image = models.ImageField(blank=True, null=True, upload_to='Post/images/webp',max_length=500, verbose_name='Image')
    imageSource = models.CharField(max_length=100, blank=True, null=True, verbose_name='Image Source')
    videoLink = models.CharField(max_length=200,null=True,blank=True, verbose_name='Video Link')
    videoSource = models.CharField(max_length=100, blank=True, null=True, verbose_name='Video Source')
    tag = models.ManyToManyField(PostsTag, blank=True, verbose_name='Tags')
    reported_by = models.ForeignKey(Reporter, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Reporter')
    written_by = models.ForeignKey(ArticleWritter, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Written By')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated At')
    status = models.IntegerField(choices=STATUS, default = 0, verbose_name='Status')
    editor_reviewed = models.IntegerField(choices=YESNO, default = 0, verbose_name='Editor Reviewed')
    total_view = models.PositiveIntegerField(default=0, verbose_name='Total View(*Do not edit)')

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Feature Posts'
        verbose_name = 'Feature Post'

    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        if not self.uniqueId or not self.uniqueId.strip():
            uid = f"{self.feature.uniqueId}{self.category.uniqueId}{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))}"
            self.uniqueId = slugify(uid).replace("-", "")
        super(FeaturePost, self).save(*args, **kwargs)
        
    