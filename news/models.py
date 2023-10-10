from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


from reporter.models import Reporter
from categories.models import *

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
YESNO = (
    (0,"No"),
    (1,"Yes")
)


class Post(models.Model):
    uniqueId = models.CharField(max_length=100,  blank=True, null=True)
    categoryId = models.ForeignKey(NewsCategory, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Category')
    subcategoryId = models.ForeignKey(NewsSubCategory, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Sub Category')
    title = models.CharField(max_length=200,  blank=True, null=True, verbose_name='Title')
    details = RichTextField(blank=True, null=True, verbose_name='Details')
    related_post = models.ManyToManyField('self', blank=True, verbose_name='Related Post Suggation')
    continent = models.ForeignKey(Continents, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Continent')
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
    
    videoLink = models.CharField(max_length=200,null=True,blank=True, verbose_name='Video Link')
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Reporter')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated At')
    status = models.IntegerField(choices=STATUS, default = 0, verbose_name='Status')
    editor_reviewed = models.IntegerField(choices=YESNO, default = 0, verbose_name='Editor Reviewed')
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True, verbose_name='URL(will be auto generated)')
    total_view = models.PositiveIntegerField(default=0, verbose_name='Total View(*Do not edit)')

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

        # if self.image0:
        #     img = Image.open(self.image0)
        #     output = BytesIO()
        #     img.convert('RGB').save(output, format='webp', maxsize=(800, 800))
        #     self.image0 = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.image.name.split('.')[0], 'News/Post/images/webp', output.getvalue(), None)
        # super(Post, self).save(*args, **kwargs)
    
        if self.uniqueId == " " or self.uniqueId == "" or self.uniqueId == None:
            self.uniqueId = str(self.id)+self.categoryId.uniqueId+self.subcategoryId.uniqueId+self.country.uniqueId
            return super().save(*args, **kwargs)
    # for url
        if not self.url:
            self.url = self.uniqueId.replace(" ", "").replace(",", "").replace("-","").replace(":", "").replace(";", "").replace("?", "").replace("!", "").replace(".", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("/", "").replace("\\", "").replace("|", "").replace("<", "").replace(">", "").replace("=", "").replace("+", "").replace("*", "").replace("&", "").replace("^", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")
            return super().save(*args, **kwargs)
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "").replace("-","").replace(":", "").replace(";", "").replace("?", "").replace("!", "").replace(".", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("/", "").replace("\\", "").replace("|", "").replace("<", "").replace(">", "").replace("=", "").replace("+", "").replace("*", "").replace("&", "").replace("^", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")
            return super().save(*args, **kwargs)
        
    # def update_filename(instance, filename):
    #     path = "upload/path/"
    #     name = instance.uniqueId
    #     format = name + instance.file_extension
    #     return os.path.join(path, format)


