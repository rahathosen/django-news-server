from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from reporter.models import Reporter

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)

class Continent(models.Model):
    uniqueId = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Continent Name in English without Space')
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Continent Name')
    image = models.ImageField(upload_to='News/Categories/Continents/',blank=True, null=True)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Continents'
        verbose_name = 'Continent'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Continent, self).save(*args, **kwargs)      
    
class Country(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Country Name in English without Space')
    cCode = models.CharField(unique=True, max_length=4, blank=True, null=True, verbose_name='Country Code')
    continent = models.ForeignKey(Continent, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Country Name')
    capital = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Country/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
  
    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Country, self).save(*args, **kwargs)

class Division(models.Model):
    uniqueId = models.CharField(unique=True,max_length=50, blank=False, null=False, verbose_name='Division Name')
    country = models.ForeignKey(Country, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Division/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Divisions'
        verbose_name = 'Division'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Division, self).save(*args, **kwargs)
        
class District(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='District Name in English without Space')
    division = models.ForeignKey(Division, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='District Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True, verbose_name='District Name')
    image = models.ImageField(upload_to='News/Categories/District/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Districts'
        verbose_name = 'District'
   
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(District, self).save(*args, **kwargs)
        
class CityCorporation(models.Model):
    uniqueId = models.CharField(unique=True,max_length=50, blank=False, null=False, verbose_name='City Corporation Name in English without Space')
    division = models.ForeignKey(Division, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='City Corporation Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/CityCorporation/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'City Corporations'
        verbose_name = 'City Corporation'
   
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(CityCorporation, self).save(*args, **kwargs)
        
class Upozila(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Upozila Name in English without Space')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Upozila Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Upozila/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Upozilas'
        verbose_name = 'Upozila'
   
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Upozila, self).save(*args, **kwargs)

class Pourosava(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Pourosava Name in English without Space')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Pourosava Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Pourosava/',blank=True, null=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Pourosavas'
        verbose_name = 'Pourosava'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Pourosava, self).save(*args, **kwargs)
    
class Thana(models.Model):
    uniqueId = models.CharField(unique= True, max_length=50, blank=False, null=False, verbose_name='Thana Name in English without Space')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    cityCorporation = models.ForeignKey(CityCorporation, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null = True)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Thana Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Thana/',blank=True, null=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Thanas'
        verbose_name = 'Thana'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Thana, self).save(*args, **kwargs)

class Union(models.Model):
    uniqueId = models.CharField(unique = True, max_length=50, blank=False, null=False, verbose_name='Union Name in English without Space')
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Union Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Union/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Unions'
        verbose_name = 'Union'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(Union, self).save(*args, **kwargs)

class ZipPostalCode(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Zip Postal Code + Name in English without Space')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False)
    cityCorporation = models.ForeignKey(CityCorporation, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null = True)
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Post office Name')
    zipCode = models.CharField(unique=True, max_length=20, blank=False, null=False, verbose_name='Zip Postal Code')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/ZipPostalCode/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["zipCode"]
        verbose_name_plural = 'Zip Postal Codes'
        verbose_name = 'Zip Postal Code'
   
    def __str__(self):
        return self.zipCode + ' - ' + ' - District: ' + str(self.district.name)
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(ZipPostalCode, self).save(*args, **kwargs)
    
class TurisumSpot(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Tourist Spot Name in English without Space')
    district = models.ForeignKey(District, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False)
    cityCorporation = models.ForeignKey(CityCorporation, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    upozila = models.ForeignKey(Upozila, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null = True)
    zipCode = models.ForeignKey(ZipPostalCode, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    union = models.ForeignKey(Union, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/TurisumSpot/',blank=True, null=True)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Turisum Spots'
        verbose_name = 'Turisum Spot'

    def __str__(self):
        return self.name + ' - District: ' + str(self.district.name)
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(TurisumSpot, self).save(*args, **kwargs)
        
class NewsCategory(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Category Name in English without Space')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Category Name')
    image = models.ImageField(upload_to='News/Categories/Category/',blank=True, null=True)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 1)
    serial = models.PositiveIntegerField(default=0,blank=True, null=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'News Categories'
        verbose_name = 'News Category'
   
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(NewsCategory, self).save(*args, **kwargs)
  
class NewsSubCategory(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Sub Category Name in English without Space')
    category = models.ForeignKey(NewsCategory, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='News/Categories/SubCategory/',blank=True, null=True)
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 1)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)
   
    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'News Sub Categories'
        verbose_name = 'News Sub Category'
   
    def __str__(self):
        return self.title + ' - Category: ' + str(self.category.title)
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(NewsSubCategory, self).save(*args, **kwargs)

class PostsTag(models.Model):
    uniqueId = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name='Tag Name in English without Space')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tag Name')
    sortDetails = models.CharField(max_length=200, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='News/Categories/Tags/',blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default = 1)
    serial = models.PositiveIntegerField(default=0,blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = 'Post Tags'
        verbose_name = 'Post Tag'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.uniqueId:
            self.uniqueId = self.uniqueId.replace(" ", "-")
        super(PostsTag, self).save(*args, **kwargs)


