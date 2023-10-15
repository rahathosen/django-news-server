import graphene
from graphene_django import DjangoObjectType

from categories.models import *
from news.models import *
from reporter.models import *
from news.apiSchema import *

class NewsCategoryType(DjangoObjectType):
    class Meta:
        model = NewsCategory
        fields = "__all__"

class NewsSubCategoryType(DjangoObjectType):
    class Meta:
        model = NewsSubCategory
        fields = "__all__"

class ContinentType(DjangoObjectType):
    class Meta:
        model = Continent
        fields = "__all__"

class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = "__all__"

class DivisionType(DjangoObjectType):
    class Meta:
        model = Division
        fields = "__all__"

class DistrictType(DjangoObjectType):
    class Meta:
        model = District
        fields = "__all__"

class CityCorporationType(DjangoObjectType):
    class Meta:
        model = CityCorporation
        fields = "__all__"

class UpozilaType(DjangoObjectType):
    class Meta:
        model = Upozila
        fields = "__all__"

class ZipPostalCodeType(DjangoObjectType):
    class Meta:
        model = ZipPostalCode
        fields = "__all__"

class PostsTagType(DjangoObjectType):
    class Meta:
        model = PostsTag
        fields = "__all__"

class Query(graphene.ObjectType):
    news_categories = graphene.List(NewsCategoryType, first = graphene.Int(), skip = graphene.Int())
    news_category = graphene.Field(NewsCategoryType, id=graphene.Int())
    news_sub_categories = graphene.List(NewsSubCategoryType, first = graphene.Int(), skip = graphene.Int())
    news_sub_category = graphene.Field(NewsSubCategoryType, id=graphene.Int())
    Continent = graphene.List(ContinentType, first = graphene.Int(), skip = graphene.Int())
    continent = graphene.Field(ContinentType, id=graphene.Int())
    countries = graphene.List(CountryType, first = graphene.Int(), skip = graphene.Int())
    country = graphene.Field(CountryType, id=graphene.Int())
    divisions = graphene.List(DivisionType, first = graphene.Int(), skip = graphene.Int())
    division = graphene.Field(DivisionType, id=graphene.Int())
    districts = graphene.List(DistrictType, first = graphene.Int(), skip = graphene.Int())
    district = graphene.Field(DistrictType, id=graphene.Int())
    cityCorporations = graphene.List(DistrictType, first = graphene.Int(), skip = graphene.Int())
    cityCorporation = graphene.Field(DistrictType, id=graphene.Int())
    upozilas = graphene.List(UpozilaType, first = graphene.Int(), skip = graphene.Int())
    upozila = graphene.Field(UpozilaType, id=graphene.Int())
    zip_postal_codes = graphene.List(ZipPostalCodeType, first = graphene.Int(), skip = graphene.Int())
    zip_postal_code = graphene.Field(ZipPostalCodeType, id=graphene.Int())
    posts_tags = graphene.List(PostsTagType, first = graphene.Int(), skip = graphene.Int())
    posts_tag = graphene.Field(PostsTagType, id=graphene.Int())

    def resolve_news_categories(self, info, first=None, skip=None, **kwargs):
        news_categories = NewsCategory.objects.all()
        if skip:
            news_categories = news_categories[skip:]
        if first:
            news_categories = news_categories[:first]

        return news_categories
    
    def resolve_news_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = NewsCategory.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_news_sub_categories(self, info, first=None, skip=None, **kwargs):
        news_sub_categories = NewsSubCategory.objects.all()
        if skip:
            news_sub_categories = news_sub_categories[skip:]
        if first:
            news_sub_categories = news_sub_categories[:first]

        return news_sub_categories
    
    def resolve_news_sub_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = NewsSubCategory.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_Continent(self, info, first=None, skip=None, **kwargs):
        Continent = Continent.objects.all()
        if skip:
            Continent = Continent[skip:]
        if first:
            Continent = Continent[:first]

        return Continent
    
    def resolve_continent(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Continent.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj            
        return None
    
    def resolve_countries(self, info, first=None, skip=None, **kwargs):
        countries = Country.objects.all()
        if skip:
            countries = countries[skip:]
        if first:
            countries = countries[:first]

        return countries
    
    def resolve_country(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Country.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_divisions(self, info, first=None, skip=None, **kwargs):
        divisions = Division.objects.all()
        if skip:
            divisions = divisions[skip:]
        if first:
            divisions = divisions[:first]

        return divisions
    
    def resolve_division(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Division.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_districts(self, info, first=None, skip=None, **kwargs):
        districts = District.objects.all()
        if skip:
            districts = districts[skip:]
        if first:
            districts = districts[:first]

        return districts
    
    def resolve_district(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = District.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_city_corporations(self, info, first=None, skip=None, **kwargs):
        city_corporations = CityCorporation.objects.all()
        if skip:
            city_corporations = city_corporations[skip:]
        if first:
            city_corporations = city_corporations[:first]

        return city_corporations
    
    def resolve_city_corporation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = CityCorporation.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_upozilas(self, info, first=None, skip=None, **kwargs):
        upozilas = Upozila.objects.all()
        if skip:
            upozilas = upozilas[skip:]
        if first:
            upozilas = upozilas[:first]

        return upozilas
    
    def resolve_upozila(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Upozila.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_zip_postal_codes(self, info, first=None, skip=None, **kwargs):
        zip_postal_codes = ZipPostalCode.objects.all()
        if skip:
            zip_postal_codes = zip_postal_codes[skip:]
        if first:
            zip_postal_codes = zip_postal_codes[:first]

        return zip_postal_codes
    
    def resolve_zip_postal_code(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = ZipPostalCode.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_posts_tags(self, info, first=None, skip=None, **kwargs):
        posts_tags = PostsTag.objects.all()
        if skip:
            posts_tags = posts_tags[skip:]
        if first:
            posts_tags = posts_tags[:first]

        return posts_tags
    
    def resolve_posts_tag(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = PostsTag.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
schema = graphene.Schema(query=Query)

# Test Query

# News Category Query
# query {
#   newsCategories {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# News Sub Category Query
# query {
#   newsSubCategories {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Continent Query
# query {
#   Continent {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Country Query
# query {
#   countries {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Division Query
# query {
#   divisions {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# District Query
# query {
#   districts {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Upozila Query
# query {
#   upozilas {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Zip Postal Code Query
# query {
#   zipPostalCodes {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Posts Tag Query
# query {
#   postsTags {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

# Single Query
# query {
#   newsCategory(id: 1) {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }

#   newsSubCategory(id: 1) {
#     id
#     name
#     details
#     image
#     url
#     totalView
#   }
