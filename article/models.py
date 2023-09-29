from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from reporter.models import Reporter
from categories.models import PostsTag

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
    # language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, blank=False, null=False, default= 1)
    name = models.CharField(max_length=200,  blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Category/',max_length=500)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
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
            slug_str = f"{self.title}"
            self.url = self.title.replace(" ", "-").replace(",", "")
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)

class ArticleWritter(models.Model):
    name = models.CharField(max_length=200,  blank=True, null=True)
    Image = models.ImageField(blank=True, null=True, upload_to='Article/Writer/',max_length=500)
    details = RichTextField(blank=True, null=True)
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
            slug_str = f"{self.title}"
            self.url = self.title.replace(" ", "-").replace(",", "")
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    # language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, blank=False, null=False, default= 1)
    title = models.CharField(max_length=200,  blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, default=1, blank=False, null=False)
    writter = models.ForeignKey(ArticleWritter, on_delete=models.DO_NOTHING, default=1, blank=False, null=False)
    tag = models.ManyToManyField(PostsTag, blank=False)
    details = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Article/Images',max_length=500)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING, blank=False, null=False)
    status = models.IntegerField(choices=STATUS, default = 0)
    editor_reviewed = models.IntegerField(choices=YESNO, default = 0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    total_view = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):        
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'Article/images/webp', output.getvalue(), None)
        super(Article, self).save(*args, **kwargs)
    # for url
        if not self.url:
            slug_str = f"{self.title}"
            self.url = self.title.replace(" ", "-").replace(",", "")
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title + ' - ' + str(self.category.name) + ' - ' + str(self.writter.name)


