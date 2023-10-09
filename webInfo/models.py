from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError

from reporter.models import Reporter
from news.models import Post
from categories.models import *
from article.models import ArticleCategory, ArticleWritter, Article 
from feature.models import Feature, FeatureCategory, FeaturePost
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)


class WebsiteInfo(models.Model):
    # language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, blank=False, null=False, default= 1)
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Website Title')
    tagLine = models.TextField(blank=True, default= "", verbose_name='Tag Line/ Slogan')
    url = models.CharField(max_length=50,blank=True, default= "", verbose_name='Website URL' )
    logo = models.ImageField(upload_to='website_info/logo',blank=True, default= "", verbose_name='Website Logo' )
    favicon = models.ImageField(upload_to='website_info/icon',blank=True, default= "", verbose_name='Website Favicon icon')
    newsThumbnail = models.ImageField(upload_to='website_info/newsThumbnail',blank=True, default= "", verbose_name='News Thumbnail')
    facebook_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Facebook URL' )
    twitter_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Twitter URL' )
    youtube_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Youtube URL' )
    instagram_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Instagram URL' )
    address = models.CharField(max_length=200,blank=True, default= "", verbose_name='Address')
    contact1 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 1')
    contact2 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 2')
    email = models.CharField(max_length=200,blank=True, default= "", verbose_name='Email Address')
    whatsapp = models.CharField(max_length=200,blank=True, default= "", verbose_name='Whatsapp Number')
    copyright_text = models.CharField(max_length=500, default= "")
    about_us = RichTextField(blank=True, default= "")
    contact_us = RichTextField(blank=True, default= "")
    advertisement_policy = RichTextField(blank=True, default= "")
    privacy_policy = RichTextField(blank=True,  verbose_name='Privacy Policy / Terms of Use', default= "")
    comment_policy = RichTextField(blank=True,  default= "")
    android_app_url = models.CharField(max_length=200,blank=True, default= "")
    ios_app_url = models.CharField(max_length=200,blank=True, default= "")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Website Info'
        verbose_name = 'Website Info'


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.newsThumbnail:
            img = Image.open(self.newsThumbnail)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.newsThumbnail = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'website_info/newsThumbnail', output.getvalue(), None)
        super(WebsiteInfo, self).save(*args, **kwargs)

class Navigation(models.Model):
    in_news = models.ManyToManyField(Continents, blank=True, verbose_name='In Nav News')
    in_news2 = models.ManyToManyField(Country, blank=True, verbose_name='In Nav News')
    in_news3 = models.ManyToManyField(Division, blank=True, verbose_name='In Nav News')
    in_news4 = models.ManyToManyField(District, blank=True, verbose_name='In Nav News')
    in_news5 = models.ManyToManyField(CityCorporation, blank=True, verbose_name='In Nav News')
    in_news6 = models.ManyToManyField(TurisumSpot, blank=True, verbose_name='In Nav News')
    in_categories = models.ManyToManyField(NewsCategory, blank=True, verbose_name='In Nav Categories', limit_choices_to= 8)
    feature = models.ManyToManyField(Feature, blank=True, verbose_name='In News feature')

    class Meta:
        verbose_name_plural = 'Navigation Bar'
        verbose_name = 'Navigation Bar'  

class HeadLine(models.Model):
    items = models.ManyToManyField(Post, blank=True , limit_choices_to = 10, verbose_name='Headlines')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Headlines / শিরোনাম'
        verbose_name = 'Headline / শিরোনাম'

    def __str__(self):
        return 'Last updated' + ' - ' + self.updated_at
    
class BreakingNews(models.Model):
    items = models.ManyToManyField(Post, blank=True, limit_choices_to = 5, verbose_name='Breaking News')
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(blank=False)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Breaking News'
        verbose_name = 'Breaking News'

    def __str__(self):
        return 'Last updated' + ' - ' + self.updated_at
    
class Cover(models.Model):
    headNews = models.ForeignKey(Post, on_delete=models.DO_NOTHING, blank=False, verbose_name='Head Line News')
    # SideBoxitems = models.ManyToManyField(Post, blank=True, verbose_name='Side Box items')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Cover / প্রচ্ছদ'
        verbose_name = 'Cover / প্রচ্ছদ'
        

    def __str__(self):
        return self.headNews.title + ' - ' + self.updated_at

    
class SectionBox(models.Model):
    background_color = models.CharField(max_length=10,blank=True, verbose_name='Background Color(Must be in Hexadecimal)')
    image = models.ImageField(upload_to='sectionBox/images/webp',blank=True, null=True)
    title = models.CharField(max_length=50,blank=False)
    details = models.TextField(blank=True, null=True)
    heighlighted = models.ForeignKey(Post, on_delete=models.DO_NOTHING, blank=False, verbose_name='Heighlighted News')
    items = models.ManyToManyField(NewsCategory, blank=True, limit_choices_to= 1)
    items2 = models.ManyToManyField(NewsSubCategory, blank=True)
    items3 = models.ManyToManyField(PostsTag, blank=True)
    items4 = models.ManyToManyField(Continents, blank=True)
    items5 = models.ManyToManyField(Country, blank=True)
    items6 = models.ManyToManyField(Division, blank=True)
    items7 = models.ManyToManyField(District, blank=True)
    items8 = models.ManyToManyField(CityCorporation, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Section Boxs'
        verbose_name = 'Section Box'

    def __str__(self):
        return self.title + ' - ' + self.updated_at
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'sectionBox/images/webp', output.getvalue(), None)
        super(SectionBox, self).save(*args, **kwargs)

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.PositiveIntegerField(default=0)
    option_two_count = models.PositiveIntegerField(default=0)
    option_three_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(blank=False)
    total_view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        self.total_view = self.total_view + 1
        super().save(*args, **kwargs)
        