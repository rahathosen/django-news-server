from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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

def convert_to_webp(image_field):
    if image_field and image_field.name.split('.')[-1] == 'webp':
        img = Image.open(image_field)
        output = BytesIO()
        img = img.convert('RGB')
        img.save(output, format='WEBP', quality=95, subsampling=0)
        output.seek(0)
        image_field = InMemoryUploadedFile(output, 'ImageField', f"{image_field.name.split('.')[0]}.webp", 'images/webp', output.read(), None)
    return image_field

class Feature(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Feature Name in English without Space')
    title = models.CharField(max_length=50)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Feature/',blank=True, null=True)
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
        self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)   


class FeatureCategory(models.Model):
    uniqueId = models.CharField( unique=True, max_length=20, blank=False, null=False, verbose_name='Category Name in English without Space')
    feature = models.ForeignKey(Feature, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature')
    title = models.CharField(max_length=50)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Feature/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["serial"]
        verbose_name_plural = 'Feature Categories'
        verbose_name = 'Feature Category'

    def __str__(self):
        return self.title + self.feature.title
    
    def save(self, *args, **kwargs):
        self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)   

class FeaturePost(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100,  blank=True, null=True)
    featureId = models.ForeignKey(Feature, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature')
    categoryId = models.ForeignKey(FeatureCategory, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Feature Category')
    title = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Title')
    details = RichTextField(blank=True, null=True, verbose_name='Details')
    related_post = models.ManyToManyField('self', blank=True, verbose_name='Related Post Suggation')
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Continent')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Country')
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Division')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='District')
    city_corporation = models.ForeignKey(CityCorporation, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='City Corporation')
    upozila = models.ForeignKey(Upozila, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Upozila')
    pourosava = models.ForeignKey(Pourosava, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Pourosava')
    thana = models.ForeignKey(Thana, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Thana')
    union = models.ForeignKey(Union, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Union')
    zip_code = models.ForeignKey(ZipPostalCode, on_delete=models.DO_NOTHING, blank=True, null= True, verbose_name='Zip Code')
    turisum_spot = models.ForeignKey(TurisumSpot, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Turisum Spot')
    tag = models.ManyToManyField(PostsTag, blank=True, verbose_name='Tags')
    image = models.ImageField(blank=True, null=True, upload_to='Post/images/webp',max_length=500, verbose_name='Image')
    imageSource = models.CharField(max_length=100, blank=True, null=True, verbose_name='Image Source')
    videoLink = models.CharField(max_length=200,null=True,blank=True, verbose_name='Video Link')
    videoSource = models.CharField(max_length=100, blank=True, null=True, verbose_name='Video Source')
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Reporter')
    written_by = models.ForeignKey(ArticleWritter, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Written By')
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
        return self.title + ' - ' + str(self.categoryId.title) + ' - ' + str(self.featureId.title)
    
    def save(self, *args, **kwargs):
        # for image
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'News/Post/images/webp', output.getvalue(), None)
        super(FeaturePost, self).save(*args, **kwargs)
    
        if self.uniqueId == " " or self.uniqueId == "" or self.uniqueId == None:
            self.uniqueId = self.featureId.uniqueId+self.categoryId.uniqueId+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
            return super().save(*args, **kwargs)
    