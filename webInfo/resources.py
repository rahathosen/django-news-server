from import_export import resources

from news.models import *
from reporter.models import *
from article.models import *
from webInfo.models import *
from categories.apiSchema import *

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('reported_by', 'category', 'subcategory', 'continent', 'country', 'title', 'description', 'division', 'district',
                  'city_corporation', 'upozila', 'pourosava', 'thana', 'image',  'tag', 'editor_reviewed',
                    'status', 'total_view')

class ReporterResource(resources.ModelResource):
    class Meta:
        model = Reporter
        fields = ('uniqueId', 'name', 'designation', 'email', 'phone', 'address', 'image' , 'details', 'total_view')

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
        fields = ('uniqueId',  'category', 'writter', 'reported_by', 'title', 'description', 'details', 'image', 'tag', 'related_article', 'editor_reviewed', 'status', 'total_view')

class ArticleCategoryResource(resources.ModelResource):
    class Meta:
        model = ArticleCategory
        fields = ('uniqueId', 'name', 'details', 'image', 'url', 'serial', 'total_view')

class ArticleWritterResource(resources.ModelResource):
    class Meta:
        model = ArticleWritter
        fields = ('uniqueId', 'name', 'Image', 'details', 'url', 'serial', 'total_view')

class PostCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsCategory
        fields = ('uniqueId', 'title', 'sortDetails', 'image', 'url', 'serial', 'total_view')

class PostSubCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsSubCategory
        fields = ('uniqueId', 'category', 'title', 'sortDetails', 'image', 'url', 'serial', 'total_view')

class PostTagResource(resources.ModelResource):
    class Meta:
        model = PostsTag
        fields = ('uniqueId', 'title', 'sortDetails', 'details', 'url', 'serial', 'total_view')

class ContinentResource(resources.ModelResource):
    class Meta:
        model = Continent
        fields = ('uniqueId', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        fields = ('uniqueId', 'cCode', 'continent', 'name', 'capital', 'currency', 'language', 'sortDetails', 'url', 'serial', 'total_view')

class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
        fields = ('uniqueId', 'country', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        fields = ('uniqueId', 'division', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class CityCorporationResource(resources.ModelResource):
    class Meta:
        model = CityCorporation
        fields = ('uniqueId', 'division', 'district', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class UpozilaResource(resources.ModelResource):
    class Meta:
        model = Upozila
        fields = ('uniqueId', 'district', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class PourosavaResource(resources.ModelResource):
    class Meta:
        model = Pourosava
        fields = ('uniqueId', 'upozila', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class ThanaResource(resources.ModelResource):
    class Meta:
        model = Thana
        fields = ('uniqueId', 'district', 'cityCorporation', 'upozila', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
        fields = ('uniqueId', 'upozila', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class ZipPostalCodeResource(resources.ModelResource):
    class Meta:
        model = ZipPostalCode
        fields = ('uniqueId', 'country', 'division', 'district', 'cityCorporation', 'upozila', 'pourosava', 'thana', 'union', 'name', 'sortDetails', 'url', 'serial', 'total_view')

class TurisumSpotResource(resources.ModelResource):
    class Meta:
        model = TurisumSpot
        fields = ('uniqueId', 'district', 'cityCorporation', 'upozila', 'union', 'zipCode', 'name', 'sortDetails',  'details', 'url', 'total_view')

