from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import piexif

from reporter.models import Reporter
from categories.models import *

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
YESNO = (
    (0, "No"),
    (1, "Yes")
)

OWN_WATERMARK_PATH = ""  # Update with your watermark path
OWN_WATERMARK_TEXT = "Your Watermark Text"


class Post(models.Model):
    uniqueId = models.CharField(max_length=100, blank=True, null=True)
    categoryId = models.ForeignKey(NewsCategory, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Category')
    subcategoryId = models.ForeignKey(NewsSubCategory, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Sub Category')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Title')
    details = RichTextField(blank=True, null=True, verbose_name='Details')
    related_post = models.ManyToManyField('self', blank=True, verbose_name='Related Post Suggestion')
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Continent')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Country')
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Division')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='District')
    city_corporation = models.ForeignKey(CityCorporation, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='City Corporation')
    upozila = models.ForeignKey(Upozila, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Upozila')
    pourosava = models.ForeignKey(Pourosava, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Pourosava')
    thana = models.ForeignKey(Thana, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Thana')
    union = models.ForeignKey(Union, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Union')
    zip_code = models.ForeignKey(ZipPostalCode, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Zip Code')
    turisum_spot = models.ForeignKey(TurisumSpot, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Tourism Spot')
    tag = models.ManyToManyField(PostsTag, blank=True, verbose_name='Tags')
    image = models.ImageField(blank=True, null=True, verbose_name='Image')
    
    videoLink = models.CharField(max_length=200,null=True,blank=True, verbose_name='Video Link')
    reported_by = models.ForeignKey(Reporter, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Reporter')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated At')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='Status')
    editor_reviewed = models.IntegerField(choices=YESNO, default=0, verbose_name='Editor Reviewed')
    url = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True, verbose_name='URL (will be auto-generated)')
    total_view = models.PositiveIntegerField(default=0, verbose_name='Total View (*Do not edit)')


    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Post'
        verbose_name_plural = 'All Posts'

    def __str__(self):
        return f"{self.title} - {self.categoryId.title} - {self.subcategoryId.title}"

    def remove_exif(self, image_data):
        exif_dict = piexif.load(image_data)
        exif_dict.pop("thumbnail", None)
        exif_bytes = piexif.dump(exif_dict)
        return exif_bytes

    # def add_watermark(self, img, watermark_path, watermark_text):
    #     if watermark_path:
    #         watermark = Image.open(watermark_path)
    #         width, height = img.size
    #         watermark_size = (int(width * 0.1), int(height * 0.1))
    #         watermark = watermark.resize(watermark_size, Image.ANTIALIAS)
    #         img.paste(watermark, (width - watermark.width, height - watermark.height), watermark)
            
    #     else:
    #         width, height = img.size
    #         watermark_font = ImageFont.truetype("arial.ttf", int(min(width, height) * 0.1))
    #         draw = ImageDraw.Draw(img)
    #         text_width, text_height = draw.textsize(watermark_text, watermark_font)
    #         x = (width - text_width) // 2
    #         y = (height - text_height) // 2
    #         draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=watermark_font)
    #     return img


    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            # Create an InMemoryUploadedFile 
            img = img.convert('RGB')
            img_data = BytesIO()
            img.save(img_data, format='webp')
            img_data.seek(0)
            img_bytes = img_data.read()

            # Remove Exif data
            # img_bytes = self.remove_exif(img_bytes)

            # Add a watermark
            watermark_text = OWN_WATERMARK_TEXT
            watermark_path = OWN_WATERMARK_PATH  # Change to the actual path of your watermark image
            img = Image.open(BytesIO(img_bytes))
            # img = self.add_watermark(img, watermark_path, watermark_text)
            # Create an InMemoryUploadedFile and save it to self._image
            self.image = InMemoryUploadedFile(BytesIO(img_bytes), None, f"{self.image.name.split('.')[0]}.webp", 'image/webp', len(img_bytes), None)
            self.imageurl = self.image.url

        super(Post, self).save(*args, **kwargs)

        if self.uniqueId == " " or self.uniqueId == "" or self.uniqueId is None:
            self.uniqueId = f"{self.id+self.categoryId.uniqueId+self.subcategoryId.uniqueId+self.country.uniqueId}"
            super(Post, self).save(*args, **kwargs)

        # For URL
        if not self.url:
            ur = f"{self.country+self.categoryId+self.title}"
            self.url = ur.replace(" ", "").replace(",", "").replace("-", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "").replace(".", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("/", "").replace("\\", "").replace("|", "").replace("<", "").replace(">", "").replace("=", "").replace("+", "").replace("*", "").replace("&", "").replace("^", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")
            super().save(*args, **kwargs)
        if self.url:
            self.url = self.url.replace(" ", "").replace(",", "").replace("-", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "").replace(".", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("/", "").replace("\\", "").replace("|", "").replace("<", "").replace(">", "").replace("=", "").replace("+", "").replace("*", "").replace("&", "").replace("^", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "")
            super(Post, self).save(*args, **kwargs)
