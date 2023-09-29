from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from reporter.models import Reporter
from categories.models import NewsCategory, NewsSubCategory, Continents, Country, Division, District, Upozila, ZipPostalCode, PostsTag

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)


class Post(models.Model):
    categoryId = models.ForeignKey(NewsCategory, on_delete=models.DO_NOTHING,default=1, blank=False, null=False)
    subcategoryId = models.ForeignKey(NewsSubCategory, on_delete=models.DO_NOTHING,default=1, blank=False, null=False)
    continent = models.ForeignKey(Continents, on_delete=models.DO_NOTHING,default=1, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING,default=1, blank=False, null=False)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING,default=1, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING,default=1, blank=True, null=True)
    upozila = models.ForeignKey(Upozila, on_delete=models.DO_NOTHING,default=1, blank=True, null=True)
    zip_code = models.ForeignKey(ZipPostalCode, on_delete=models.DO_NOTHING,default=1, blank=True, null= True)
    title = models.CharField(max_length=200,  blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    tag = models.ManyToManyField(PostsTag, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='Post/images/webp',max_length=500)
    videoLink = models.CharField(max_length=200,null=True,blank=True)
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING,default=1, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    editor_reviewed = models.IntegerField(choices=YESNO, default = 0)
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    total_view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Post'
        verbose_name_plural = 'All Posts'

    def __str__(self):
        return self.title + ' - ' + str(self.categoryId.title) + ' - ' + str(self.subcategoryId.title)
   
    def save(self, *args, **kwargs):
        # for image
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'News/Post/images/webp', output.getvalue(), None)
        super(Post, self).save(*args, **kwargs)
    # for url
        if not self.url:
            slug_str = f"{self.title}"
            self.url = self.title.replace(" ", "-").replace(",", "")
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "")
        return super().save(*args, **kwargs)


