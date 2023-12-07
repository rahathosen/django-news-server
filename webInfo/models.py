from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError

from reporter.models import *
from news.models import Post
from categories.models import *
from article.models import *
from feature.models import *
from advertisement.models import *

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
    tagLine = models.CharField(max_length=50, blank=True, default= "", verbose_name='Tag Line/ Slogan')
    url = models.CharField(max_length=50,blank=True, default= "", verbose_name='Website URL' )
    logo = models.ImageField(upload_to='website_info/logo',blank=True, default= "", verbose_name='Website Logo' )
    favicon = models.ImageField(upload_to='website_info/icon',blank=True, default= "", verbose_name='Website Favicon icon')
    newsThumbnail = models.ImageField(upload_to='website_info/newsThumbnail',blank=True, default= "", verbose_name='News Thumbnail')
    facebook_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Facebook URL' )
    twitter_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Twitter URL' )
    youtube_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Youtube URL' )
    instagram_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Instagram URL' )
    linkedin_url = models.CharField(max_length=200,blank=True, default= "", verbose_name='Linkedin URL' )
    head_editor = models.CharField(max_length=100,blank=True, default= "", verbose_name='Head Editor/ সম্পাদক ')
    editor_admin = models.CharField(max_length=100,blank=True, default= "", verbose_name='Editor admin / নির্বাহী সম্পাদক')
    editor_news = models.CharField(max_length=100,blank=True, default= "", verbose_name='News Editor/ বার্তা সম্পাদক')
    publisher = models.CharField(max_length=100,blank=True, default= "", verbose_name='Publisher/ প্রকাশক')
    address = models.CharField(max_length=200,blank=True, default= "", verbose_name='Address')
    contact1 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 1')
    contact2 = models.CharField(max_length=20,blank=True, default= "", verbose_name='Contact Nubmer 2')
    email = models.CharField(max_length=200,blank=True, default= "", verbose_name='Email Address')
    whatsapp = models.CharField(max_length=200,blank=True, default= "", verbose_name='Whatsapp Number')
    telegram = models.CharField(max_length=200,blank=True, default= "", verbose_name='Telegram Number')
    google_map = models.TextField(blank=True, default= "", verbose_name='Google Map')
    copyright_text = models.CharField(max_length=100, default= "")
    about_us = RichTextField(blank=True, default= "")
    contact_us = RichTextField(blank=True, default= "")
    advertisement_policy = RichTextField(blank=True, default= "")
    privacy_policy = RichTextField(blank=True,  verbose_name='Privacy Policy / Terms of Use', default= "")
    comment_policy = RichTextField(blank=True,  default= "")
    openion_gideline = RichTextField(blank=True,  default= "")
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
    # news = models.ManyToManyField(Continent, blank=True, verbose_name='In Nav News')
    # news2 = models.ManyToManyField(Country, blank=True, verbose_name='In Nav News')
    # news3 = models.ManyToManyField(Division, blank=True, verbose_name='In Nav News')
    # news4 = models.ManyToManyField(District, blank=True, verbose_name='In Nav News')
    # news5 = models.ManyToManyField(CityCorporation, blank=True, verbose_name='In Nav News')
    # news6 = models.ManyToManyField(TurisumSpot, blank=True, verbose_name='In Nav News')
    # openion = models.ManyToManyField(ArticleCategory, blank=True, verbose_name='In Nav Openion')
    categories = models.ManyToManyField(NewsCategory, blank=False, verbose_name='In Nav Categories(Do not select 9 more)')
    feature = models.ManyToManyField(Feature, blank=True, verbose_name='In News feature')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Navigation Bar'
        verbose_name = 'Navigation Bar'

    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"

class HeadLine(models.Model):
    headlines = models.ManyToManyField(Post, blank=True , verbose_name='Head lines')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Head lines'
        verbose_name = 'Head line'

    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"
    
class BreakingNews(models.Model):
    post = models.ForeignKey(Post, blank=False, default= 1, on_delete=models.DO_NOTHING, verbose_name='Breaking News')
    updated_at = models.DateTimeField(auto_now=True)
    end_at = models.DateTimeField(blank=False)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Breaking News'
        verbose_name = 'Breaking News'

    def __str__(self):
        return f"{self.post.title} -'Last updated' : {self.updated_at}"
    
class HeadNews(models.Model):
    headNews = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=1, blank=False, verbose_name='Head/Main News')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Head/Main News'
        verbose_name = 'Head/Main News'
        
    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"
    
class HomeHighlightedNews(models.Model):
    highlightedNews = models.ManyToManyField(Post, blank=False, verbose_name='Highlighted News')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = 'Home Highlighted News'
        verbose_name = 'Home Highlighte dNews'
        
    def __str__(self):
        return f"'Last updated' + ' - ' + {self.updated_at}"

    
class SectionBox(models.Model):
    serial = models.PositiveIntegerField(default=0, blank=False, verbose_name='Serial Number')
    background_color = models.CharField(max_length=10, blank=True, verbose_name='Background Color(Must be in Hexadecimal)')
    category = models.ForeignKey(NewsCategory, default=1, on_delete=models.DO_NOTHING, blank=False)
    image = models.ImageField(upload_to='sectionBox/images/webp',blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["serial"]
        verbose_name_plural = 'Section Boxs'
        verbose_name = 'Section Box'

    def __str__(self):
        return f"{self.category.title + '-' + str(self.updated_at)}"

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
    
