from import_export import resources

from news.models import *
from reporter.models import *
from article.models import *
from webInfo.models import *
from categories.apiSchema import *

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'uniqueId', 'reported_by', 'category', 'subcategory', 'continent', 'country', 'title', 'description', 
                  'division', 'district',
                  'city_corporation', 'upozila', 'pourosava', 'thana', 'image', 'image_source', 'video_link', 'video_source',
                    'tag', 'editor_reviewed', 'status', 'total_view')

class ReporterResource(resources.ModelResource):
    class Meta:
        model = Reporter
        fields = ('id', 'uniqueId', 'name', 'designation', 'email', 'phone', 'address', 'image' , 'details', 'total_view')

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
        fields = ('id', 'uniqueId',  'category', 'writter', 'reported_by', 'title', 'description', 'details', 'image', 'image_source',
                  'tag', 'related_article', 'editor_reviewed', 'status', 'total_view')

class ArticleCategoryResource(resources.ModelResource):
    class Meta:
        model = ArticleCategory
        fields = ('id', 'uniqueId', 'name', 'details',  'image', 'imageSource', 'serial', 'total_view')

class ArticleWritterResource(resources.ModelResource):
    class Meta:
        model = ArticleWritter
        fields = ('id', 'uniqueId', 'name', 'Image', 'details', 'serial', 'total_view')

class PostCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsCategory
        fields = ('id', 'uniqueId', 'title', 'sortDetails', 'image', 'serial', 'total_view')

class PostSubCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsSubCategory
        fields = ('id', 'uniqueId', 'category', 'title', 'sortDetails', 'image', 'serial', 'total_view')

class PostTagResource(resources.ModelResource):
    class Meta:
        model = PostsTag
        fields = ('id', 'uniqueId', 'title', 'sortDetails', 'details', 'serial', 'total_view')

class ContinentResource(resources.ModelResource):
    class Meta:
        model = Continent
        fields = ('id', 'uniqueId', 'name', 'sortDetails', 'serial', 'total_view')

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        fields = ('id', 'uniqueId', 'cCode', 'continent', 'name', 'capital', 'currency', 'language', 'sortDetails', 'serial', 'total_view')

class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
        fields = ('id', 'uniqueId', 'country', 'name', 'sortDetails', 'serial', 'total_view')

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        fields = ('id', 'uniqueId', 'division', 'name', 'sortDetails', 'serial', 'total_view')

class CityCorporationResource(resources.ModelResource):
    class Meta:
        model = CityCorporation
        fields = ('id', 'uniqueId', 'division', 'district', 'name', 'sortDetails', 'serial', 'total_view')

class UpozilaResource(resources.ModelResource):
    class Meta:
        model = Upozila
        fields = ('id', 'uniqueId', 'district', 'name', 'sortDetails', 'serial', 'total_view')

class PourosavaResource(resources.ModelResource):
    class Meta:
        model = Pourosava
        fields = ('id', 'uniqueId', 'upozila', 'name', 'sortDetails', 'serial', 'total_view')

class ThanaResource(resources.ModelResource):
    class Meta:
        model = Thana
        fields = ('id', 'uniqueId', 'district', 'cityCorporation', 'upozila', 'name', 'sortDetails', 'serial', 'total_view')

class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
        fields = ('id', 'uniqueId', 'upozila', 'name', 'sortDetails', 'serial', 'total_view')

class ZipPostalCodeResource(resources.ModelResource):
    class Meta:
        model = ZipPostalCode
        fields = ('id', 'uniqueId', 'country', 'division', 'district', 'cityCorporation', 'upozila', 'pourosava', 'thana', 
                  'union', 'name', 'sortDetails', 'serial', 'total_view')

class TurisumSpotResource(resources.ModelResource):
    class Meta:
        model = TurisumSpot
        fields = ('id', 'uniqueId', 'district', 'cityCorporation', 'upozila', 'union', 'zipCode', 'name', 'sortDetails',  'details', 'total_view')

