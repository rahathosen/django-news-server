import datetime
import graphene
from graphene_django import DjangoObjectType

from news.models import *
from reporter.models import *
from article.models import *
from webInfo.models import *
from categories.apiSchema import *

import os

def remove_file_extension(image_url):
    filename, file_extension = os.path.splitext(image_url)
    if file_extension:
        new = filename
        return new
    else:
        return image_url

 
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"
        


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int(), uId = graphene.String())
    all_posts = graphene.List(PostType)
   
    today_posts = graphene.List(PostType)
    last_week_popular_post  = graphene.List(PostType)
    last_month_popular_post = graphene.List(PostType)

    post_by_category = graphene.List(PostType, category_id=graphene.Int(), uId = graphene.String())
    post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int(), uId = graphene.String())
    post_by_country = graphene.List(PostType, country_id=graphene.Int(), uId = graphene.String())
    post_by_division = graphene.List(PostType, division_id=graphene.Int(), uId = graphene.String())
    post_by_district = graphene.List(PostType, district_id=graphene.Int(), uId = graphene.String())
    post_by_cityCorporation = graphene.List(PostType, cityCorporation_id=graphene.Int(), uId = graphene.String())
    post_by_upozila = graphene.List(PostType, upozila_id=graphene.Int())
    post_by_Thana = graphene.List(PostType, thana_id=graphene.Int())
    post_by_pourosava = graphene.List(PostType, pourosava_id=graphene.Int())
    post_by_union = graphene.List(PostType, union_id=graphene.Int())
    post_by_tourist_spot = graphene.List(PostType, tourist_spot_id=graphene.Int())
    post_by_zip_postal_code = graphene.List(PostType, zip_postal_code_id=graphene.Int())
    post_by_tag = graphene.List(PostType, tag_id=graphene.Int())
    post_by_reporter = graphene.List(PostType, author_id=graphene.Int())

    last_8_post_by_category = graphene.List(PostType, category_id=graphene.Int())
    last_8_post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int())

    top_8_post_by_category_this_week = graphene.List(PostType, category_id=graphene.Int())
    top_8_post_by_sub_category_this_week = graphene.List(PostType, sub_category_id=graphene.Int())

    filter_post = graphene.List(PostType, category_id=graphene.Int(),
                                sub_category_id=graphene.Int(), country_id=graphene.Int(), 
                                division_id=graphene.Int(), district_id=graphene.Int(), 
                                cityCorporation_id=graphene.Int(), upozila_id=graphene.Int(), 
                                zip_postal_code_id=graphene.Int(), tag_id=graphene.Int(), 
                                author_id=graphene.Int())

    
    def resolve_post(self, info, uId = None, **kwargs):
        id = kwargs.get('id')
        pk = kwargs.get('pk')
        uniqueId = kwargs.get('uniqueId')

        if uId is not None:
            obj = Post.objects.get(uniqueId=uId)
            obj.total_view = obj.total_view + 1
            obj.save()
            obj.image.name = remove_file_extension(obj.image.name)
            return obj
        
        elif id is not None:
            obj = Post.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            obj.image.name = remove_file_extension(obj.image.name)
            return obj
        
        elif uniqueId is not None:
            obj = Post.objects.get(uniqueId=uniqueId)
            obj.total_view = obj.total_view + 1
            obj.save()
            obj.image.name = remove_file_extension(obj.image.name)
            return obj
        
        elif pk is not None:
            obj = Post.objects.get(pk=pk)
            obj.total_view = obj.total_view + 1
            obj.save()
            obj.image.name = remove_file_extension(obj.image.name)
            
            return obj
        
        else:
            return None
        
    
    def resolve_all_posts(self, info, **kwargs):
        posts =  Post.objects.all()
        for post in posts:
            post.image.name = remove_file_extension(post.image.name)
        return posts
    
    def resolve_today_posts(self, info, **kwargs):
        return Post.objects.filter(created_at__date=datetime.date.today())
    
    def resolve_last_week_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7))
    
    def resolve_last_month_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30))
    

    def resolve_post_by_category(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id)
    
    def resolve_post_by_sub_category(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id)
    
    def resolve_post_by_country(self, info, country_id, **kwargs):
        return Post.objects.filter(country_id=country_id)
    
    def resolve_post_by_division(self, info, division_id, **kwargs):
        return Post.objects.filter(division_id=division_id)
    
    def resolve_post_by_district(self, info, district_id, **kwargs):
        return Post.objects.filter(district_id=district_id)
    
    def resolve_post_by_cityCorporation(self, info, cityCorporation_id, **kwargs):
        return Post.objects.filter(cityCorporation_id=cityCorporation_id)
    
    def resolve_post_by_upozila(self, info, upozila_id, **kwargs):
        return Post.objects.filter(upozila_id=upozila_id)
    
    def resolve_post_by_zip_postal_code(self, info, zip_postal_code_id, **kwargs):
        return Post.objects.filter(zip_postal_code_id=zip_postal_code_id)
    
    def resolve_post_by_tag(self, info, tag_id, **kwargs):
        return Post.objects.filter(tag_id=tag_id)
    
    def resolve_post_by_reporter(self, info, author_id, **kwargs):
        return Post.objects.filter(author_id=author_id)
    
    
    def resolve_last_8_post_by_category(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id)[:8]
    
    def resolve_last_8_post_by_sub_category(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id)[:8]
    
    
    def resolve_top_8_post_by_category_this_week(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id, created_at__gte=datetime.date.today()-datetime.timedelta(days=7))
        
    def resolve_top_8_post_by_sub_category_this_week(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id, created_at__gte=datetime.date.today()-datetime.timedelta(days=7))
    
    def resolve_filter_post(self, info, category_id, sub_category_id, country_id, division_id, district_id, cityCorporation_id, upozila_id, zip_postal_code_id, tag_id, author_id, **kwargs):
        return Post.objects.filter(category_id=category_id, sub_category_id=sub_category_id, country_id=country_id, division_id=division_id, district_id=district_id, cityCorporation_id=cityCorporation_id, upozila_id=upozila_id, zip_postal_code_id=zip_postal_code_id, tag_id=tag_id, author_id=author_id)

class PostInput(graphene.InputObjectType):
    category_id = graphene.Int(required=True)
    sub_category_id = graphene.Int(required=True)
    continent_id = graphene.Int(required=True)
    country_id = graphene.Int(required=True)
    reported_by_id = graphene.Int(required=True)
    title = graphene.String(required=True)
    details = graphene.String(required=False)
    image = graphene.String(required=False)
    videoLink = graphene.String(required=False)
    status = graphene.Int(required=True)
    editorReviewed = graphene.Int(required=True)

class CreatePost(graphene.Mutation):
    class Arguments:
        post_data = PostInput(required=True)

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, post_data=None):
        post_instance = Post(
            category_id=post_data.category_id,
            sub_category_id=post_data.sub_category_id,
            continent_id=post_data.continent_id,
            country_id=post_data.country_id,
            reported_by_id=post_data.reported_by_id,
            title=post_data.title,
            details=post_data.details,
            image=post_data.image,
            videoLink=post_data.videoLink,
            status=post_data.status,
            editorReviewed=post_data.editorReviewed,
        )
        post_instance.save()
        return CreatePost(post=post_instance)

class UpdatePost(graphene.Mutation):
    class Arguments:
        post_data = PostInput(required=True)
        id = graphene.ID()

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, post_data=None, id=None):
        post_instance = Post.objects.get(pk=id)

        if post_instance:
            post_instance.category_id = post_data.category_id
            post_instance.sub_category_id = post_data.sub_category_id
            post_instance.continent_id = post_data.continent_id
            post_instance.country_id = post_data.country_id
            post_instance.reported_by_id = post_data.reported_by_id
            post_instance.title = post_data.title
            post_instance.details = post_data.details
            post_instance.image = post_data.image
            post_instance.videoLink = post_data.videoLink
            post_instance.status = post_data.status
            post_instance.editorReviewed = post_data.editorReviewed
            post_instance.save()

            return UpdatePost(post=post_instance)
        return UpdatePost(post=None)

class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    post = graphene.Field(PostType)

    @staticmethod
    def mutate(root, info, id):
        post_instance = Post.objects.get(pk=id)
        post_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)

# Test Query

# Post Query
# query {
#   posts {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name    
#     }
#     title
#     details
#     image
#     videoLink
#     status
#     editorReviewed
#     url
#     totalView
#     createdAt
#     updated_at
#   }

#   post(id: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name
#     }
#     title
#     details
#     image
#     videoLink
#     status
#     editorReviewed
#     url
#     totalView
#     createdAt
#     updated_at
#   }
# }

# Post by category
# query {
#   postByCategory(categoryId: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name
#     }
#     title
#     details
#     image
#     videoLink
#     status
#     editorReviewed
#     url
#     totalView
#     createdAt
#     updated_at
#   }
# }

# Post by sub category
# query {
#   postBySubCategory(subCategoryId: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id

# Post by country
# query {
#   postByCountry(countryId: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name    
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name
#     }
#     title
#     details
#     image
#     videoLink 
#     status
#     editorReviewed    
#     url
#     totalView
#     createdAt
#     updated_at
#   }
# }

# Last 8 post by category Query
# query {
#   last8PostByCategory(categoryId: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name
#     }
#     title
#     details
#     image
#     videoLink
#     status
#     editorReviewed
#     url
#     totalView
#     createdAt
#     updated_at
#   }
# }

# Filter Post Query
# query {
#   filterPost(categoryId: 1, subCategoryId: 1, countryId: 1, divisionId: 1, districtId: 1, cityCorporationId: 1, upozilaId: 1, zipPostalCodeId: 1, tagId: 1, authorId: 1) {
#     id
#     category {
#       id
#       name
#     }
#     subCategory {
#       id
#       name
#     }
#     country {
#       id
#       name
#     }
#     division {
#       id
#       name
#     }
#     district {
#       id
#       name
#     }
#     cityCorporation {
#       id
#       name
#     }
#     upozila {
#       id
#       name
#     }
#     zipPostalCode {
#       id
#       name    
#     }
#     tag {
#       id
#       name
#     }
#     reported_by {
#       id
#       name
#     }
#     title
#     details
#     image 
#     videoLink
#     status
#     editorReviewed
#     url
#     totalView
#     createdAt
#     updated_at
#   }
# }

