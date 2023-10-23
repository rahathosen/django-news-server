from import_export import resources

from reporter.models import *
from advertisement.models import *
from article.models import *
from categories.models import *
from feature.models import *
from news.models import *
from reporter.models import *
from webInfo.models import *

class ArticleCategoryResource(resources.ModelResource):
    class Meta:
        model = ArticleCategory
        fields = ('id', 'uniqueId', 'name', 'details',  'image', 'serial', 'total_view')

class ArticleWritterResource(resources.ModelResource):
    class Meta:
        model = ArticleWritter
        fields = ('id', 'uniqueId', 'name', 'Image', 'details',
                  'created_at', 'updated_at', 'total_view')

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
        fields = ('id', 'uniqueId',  'category', 'writter', 'reported_by',
                  'title', 'description', 'details', 'image', 'image_source',
                  'tag', 'related_article', 'editor_reviewed', 'created_at', 
                    'updated_at', 'status', 'total_view')

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'uniqueId', 'reported_by', 'category', 'subcategory',
                   'continent', 'country', 'division', 'district', 
                   'city_corporation', 'upozila', 'pourosava', 'thana',
                    'union', 'zip_code', 'turisum_spot',
                    'title', 'description', 'details', 'related_post',
                    'image', 'image_source', 'video_link', 'video_source',
                    'tag', 'created_at', 'updated_at', 'status', 
                    'editor_reviewed', 'total_view')

class ReporterResource(resources.ModelResource):
    class Meta:
        model = Reporter
        fields = ('id', 'uniqueId', 'name', 'designation', 'email', 'phone', 'address',
                  'image' , 'details', 'created_at', 'updated_at', 'total_view')


class PostCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsCategory
        fields = ('id', 'uniqueId', 'title', 'image', 'sortDetails', 'status', 'serial', 'total_view')

class PostSubCategoryResource(resources.ModelResource):
    class Meta:
        model = NewsSubCategory
        fields = ('id', 'uniqueId', 'category', 'title', 'image', 'sortDetails', 'status', 'serial', 'total_view')

class PostTagResource(resources.ModelResource):
    class Meta:
        model = PostsTag
        fields = ('id', 'uniqueId', 'title', 'sortDetails', 'details', 
                  'image', 'serial', 'total_view')

class ContinentResource(resources.ModelResource):
    class Meta:
        model = Continent
        fields = ('id', 'uniqueId', 'name', 'sortDetails', 
                  'image', 'serial', 'total_view')

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        fields = ('id', 'uniqueId', 'cCode', 'continent', 'name', 'capital',
                  'currency', 'language', 'sortDetails', 
                  'image', 'serial', 'total_view')

class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
        fields = ('id', 'uniqueId', 'country', 'name', 'sortDetails', 
                  'image', 'serial', 'total_view')

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District
        fields = ('id', 'uniqueId', 'division', 'name', 'sortDetails', 
                  'image', 'serial', 'total_view')

class CityCorporationResource(resources.ModelResource):
    class Meta:
        model = CityCorporation
        fields = ('id', 'uniqueId', 'division', 'district', 'name', 
                  'sortDetails', 'image', 'serial', 'total_view')

class UpozilaResource(resources.ModelResource):
    class Meta:
        model = Upozila
        fields = ('id', 'uniqueId', 'district', 'name', 'sortDetails',
                  'image', 'serial', 'total_view')

class PourosavaResource(resources.ModelResource):
    class Meta:
        model = Pourosava
        fields = ('id', 'uniqueId', 'district', 'upozila', 'name', 'sortDetails',
                  'image', 'total_view')

class ThanaResource(resources.ModelResource):
    class Meta:
        model = Thana
        fields = ('id', 'uniqueId', 'district', 'cityCorporation', 'upozila', 
                  'name', 'sortDetails', 'image', 'total_view')

class UnionResource(resources.ModelResource):
    class Meta:
        model = Union
        fields = ('id', 'uniqueId', 'upozila', 'name', 'sortDetails', 
                  'image', 'serial', 'total_view')

class ZipPostalCodeResource(resources.ModelResource):
    class Meta:
        model = ZipPostalCode
        fields = ('id', 'uniqueId', 'district', 'cityCorporation', 'upozila', 
                  'name', 'zipCode', 'sortDetails', 'image', 'serial', 'total_view')

class TurisumSpotResource(resources.ModelResource):
    class Meta:
        model = TurisumSpot
        fields = ('id', 'uniqueId', 'district', 'cityCorporation', 'upozila', 
                  'zipCode', 'union', 'name', 'sortDetails',  'details', 
                  'image', 'serial', 'total_view')

class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature
        fields = ('id', 'uniqueId', 'title', 'sortDetails',
                  'details', 'image', 'serial', 'total_view',
                   'created_at', 'updated_at')

class FeatureCategoryResource(resources.ModelResource):
    class Meta:
        model = FeatureCategory
        fields = ('id', 'uniqueId', 'feature', 'title', 'sortDetails',
                  'details', 'image', 'serial', 'total_view')

class FeaturePostResource(resources.ModelResource):
    class Meta:
        model = FeaturePost
        fields = ('id', 'uniqueId', 'feature', 'category', 'continent', 
                  'country',  'division', 'district', 'city_corporation',  
                  'upozila',  'pourosava', 'thana', 'union', 'zip_code', 
                  'turisum_spot', 'title', 'description', 'details',
                  'related_post','image', 'imageSource', 'videoLink', 
                  'videoSource', 'tag', 
                  'reported_by', 'written_by', 'created_at', 'updated_at',
                  'status', 'editor_reviewed', 'total_view'
                  )

class AdBoxResource(resources.ModelResource):
    class Meta:
        model = AdBox
        fields = ('id', 'uniqueId', 'position', 'size', 'active',
                  'total_view')
        
class AdCompanyResource(resources.ModelResource):
    class Meta:
        model = AdCompany
        fields = ('id', 'uniqueId', 'name', 'image', 'link', 'payment_due',
                  'created_at', 'updated_at')

class AdvertisementResource(resources.ModelResource):
    class Meta:
        model = Advertisement
        fields = ('id', 'uniqueId', 'add_company', 'title', 'image', 'link',
                  'embed_code', 'addBox', 'status', 'created_at', 'updated_at',
                  'total_view', 'stop_at')

class WebsiteInfoResource(resources.ModelResource):
    class Meta:
        model = WebsiteInfo
        fields = ('id', 'title', 'tagLine', 'url', 'logo', 'favicon',
                  'newsThumbnail','facebook_url', 'twitter_url', 
                  'youtube_url', 'instagram_url', 'linkedin_url',
                  'address', 'contact1', 'contact2', 'email',
                  'whatsapp', 'telegram', 'google_map', 'copyright_text',
                  'about_us', 'contact_us', 'advertisement_policy',
                  'privacy_policy', 'comment_policy', 
                  'android_app_url', 'ios_app_url', 
                  'created_at', 'updated_at')

class NavMenuResource(resources.ModelResource):
    class Meta:
        model = Navigation
        fields = ('id', 'news', 'news2', 'news3', 'news4', 'news5', 'news6',
                  'categories', 'feature', 'updated_at')

class SectionResource(resources.ModelResource):
    class Meta:
        model = SectionBox
        fields = ('id', 'uniqueId', 'background_color', 'image',
                  'title', 'details', 'heighlighted', 'items', 
                  'items2', 'items3', 'items4', 'items5', 'items6',
                  'items7', 'items8', 'items9', 'items10', 'adbox_top',
                  'created_at', 'updated_at')

class HeadLineResource(resources.ModelResource):
    class Meta:
        model = HeadLine
        fields = ('id', 'headlines', 'updated_at')

class BreakingNewsResource(resources.ModelResource):
    class Meta:
        model = BreakingNews
        fields = ('id', 'items', 'updated_at', 'end_at')

class CoverResource(resources.ModelResource):
    class Meta:
        model = Cover
        fields = ('id', 'headNews', 'updated_at')

class PollResource(resources.ModelResource):
    class Meta:
        model = Poll
        fields = ('id', 'uniqueId', 'question', 
                  'option_one', 'option_two', 'option_three',
                  'option_one_count', 'option_two_count', 'option_three_count',
                  'created_at', 'updated_at', 'end_at', 'total_view')