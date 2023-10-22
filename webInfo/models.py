from django.db import models
from ckeditor.fields import RichTextField
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
    linkedin_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Linkedin URL' )
    address = models.CharField(max_length=200,blank=True, default= "", verbose_name='Address')
    contact1 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 1')
    contact2 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 2')
    email = models.CharField(max_length=200,blank=True, default= "", verbose_name='Email Address')
    whatsapp = models.CharField(max_length=200,blank=True, default= "", verbose_name='Whatsapp Number')
    telegram = models.CharField(max_length=200,blank=True, default= "", verbose_name='Telegram Number')
    google_map = models.TextField(blank=True, default= "", verbose_name='Google Map')
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

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Website Infos'
        verbose_name = 'Website Info'

    def __str__(self):
        return self.title
        
class Navigation(models.Model):
    news = models.ManyToManyField(Continent, blank=True, verbose_name='In Nav News')
    news2 = models.ManyToManyField(Country, blank=True, verbose_name='In Nav News')
    news3 = models.ManyToManyField(Division, blank=True, verbose_name='In Nav News')
    news4 = models.ManyToManyField(District, blank=True, verbose_name='In Nav News')
    news5 = models.ManyToManyField(CityCorporation, blank=True, verbose_name='In Nav News')
    news6 = models.ManyToManyField(TurisumSpot, blank=True, verbose_name='In Nav News')
    categories = models.ManyToManyField(NewsCategory, blank=False, verbose_name='In Nav Categories(Do not select 8 more)')
    feature = models.ManyToManyField(Feature, blank=True, verbose_name='In News feature')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Navigation Bar'
        verbose_name = 'Navigation Bar'

    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"

class HeadLine(models.Model):
    headlines = models.ManyToManyField(Post, blank=True , verbose_name='Headlines')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Headlines'
        verbose_name = 'Headline'

    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"
    
class BreakingNews(models.Model):
    items = models.ManyToManyField(Post, blank=True, verbose_name='Breaking News')
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(blank=False)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Breaking News'
        verbose_name = 'Breaking News'

    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"
    
class Cover(models.Model):
    headNews = models.ForeignKey(Post, to_field='uniqueId', on_delete=models.DO_NOTHING, blank=False, verbose_name='Head Line News')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Cover'
        verbose_name = 'Cover'
        
    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"

    
class SectionBox(models.Model):
    background_color = models.CharField(max_length=10, blank=True, verbose_name='Background Color(Must be in Hexadecimal)')
    image = models.ImageField(upload_to='sectionBox/images/webp',blank=True, null=True)
    title = models.CharField(max_length=50, blank=False)
    details = models.TextField(blank=True, null=True)
    heighlighted = models.ForeignKey(Post, to_field= 'uniqueId', on_delete=models.DO_NOTHING, blank=False, verbose_name='Heighlighted News')
    items = models.ManyToManyField(NewsCategory, blank=True)
    items2 = models.ManyToManyField(NewsSubCategory, blank=True)
    items3 = models.ManyToManyField(PostsTag, blank=True)
    items4 = models.ManyToManyField(Continent, blank=True)
    items5 = models.ManyToManyField(Country, blank=True)
    items6 = models.ManyToManyField(Division, blank=True)
    items7 = models.ManyToManyField(District, blank=True)
    items8 = models.ManyToManyField(CityCorporation, blank=True)
    items9 = models.ManyToManyField(ArticleCategory, blank=True)
    items10 = models.ManyToManyField(ArticleWritter, blank=True)
    serial = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Section Boxs'
        verbose_name = 'Section Box'

    def __str__(self):
        return f"{self.title + '-' + str(self.updated_at)}"

class Poll(models.Model):
    uniqueId = models.CharField(unique=True, max_length=100, blank=True, null=True)
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

    def save(self, *args, **kwargs):
        self.total_view = self.total_view + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question}"
    
    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Polls'
        verbose_name = 'Poll'
    
