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
        new = filename+'.webp'
        return new
    else:
        return image_url

 
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"
        


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int(), uId = graphene.String())
    all_posts = graphene.List(PostType, first = graphene.Int(), skip = graphene.Int())
   
    today_posts = graphene.List(PostType)
    last_week_popular_post  = graphene.List(PostType)
    last_month_popular_post = graphene.List(PostType)

    post_by_category = graphene.List(PostType, category_id=graphene.Int(), category_uId = graphene.String())
    post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int(), sub_sucategory_uId = graphene.String())
    post_by_country = graphene.List(PostType, country_id=graphene.Int(), country_uId = graphene.String())
    post_by_division = graphene.List(PostType, division_id=graphene.Int(), division_uId = graphene.String())
    post_by_district = graphene.List(PostType, district_id=graphene.Int(), district_uId = graphene.String())
    post_by_cityCorporation = graphene.List(PostType, cityCorporation_id=graphene.Int(), cityCorporation_uId = graphene.String())
    post_by_upozila = graphene.List(PostType, upozila_id=graphene.Int(), upozila_uId = graphene.String())
    post_by_Thana = graphene.List(PostType, thana_id=graphene.Int(), thana_uId = graphene.String())
    post_by_pourosava = graphene.List(PostType, pourosava_id=graphene.Int(), pourosava_uId = graphene.String())
    post_by_union = graphene.List(PostType, union_id=graphene.Int(), union_uId = graphene.String())
    post_by_tourist_spot = graphene.List(PostType, tourist_spot_id=graphene.Int(), tourist_spot_uId = graphene.String())
    post_by_zip_postal_code = graphene.List(PostType, zip_postal_code_id=graphene.Int(), zip_postal_code_uId = graphene.String())
    post_by_tag = graphene.List(PostType, tag_id=graphene.Int(), tag_uId = graphene.String())
    post_by_reporter = graphene.List(PostType, author_id=graphene.Int(), author_uId = graphene.String())

    last_8_post_by_category = graphene.List(PostType, category_id=graphene.Int(), category_uId = graphene.String()) 
    last_8_post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int(), sub_category_uId = graphene.String())

    top_8_post_by_category_this_week = graphene.List(PostType, category_id=graphene.Int(), category_uId = graphene.String())
    top_8_post_by_sub_category_this_week = graphene.List(PostType, sub_category_id=graphene.Int(), sub_category_uId = graphene.String())

    filter_post = graphene.List(PostType, category_id=graphene.Int(),
                                sub_category_id=graphene.Int(), country_id=graphene.Int(), 
                                division_id=graphene.Int(), district_id=graphene.Int(), 
                                cityCorporation_id=graphene.Int(), upozila_id=graphene.Int(), 
                                zip_postal_code_id=graphene.Int(), tag_id=graphene.Int(), 
                                author_id=graphene.Int())

    
    def resolve_post(self, info, uId, id = None, **kwargs):
        id = kwargs.get('id')
        pk = kwargs.get('pk')
        uniqueId = kwargs.get('uniqueId')

        if uId is not None:
            obj = Post.objects.get(uniqueId=uId, status = 1, editor_reviewed = 1)
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
        
    
    def resolve_all_posts(self, info, first=None, skip=None, **kwargs):
        posts =  Post.objects.all().filter(status=1, editor_reviewed=1)
        for post in posts:
            post.image.name = remove_file_extension(post.image.name)
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]
        return posts
    
    def resolve_today_posts(self, info, **kwargs):
        return Post.objects.filter(created_at__date=datetime.date.today()).filter(status=1, editor_reviewed=1)
    
    def resolve_last_week_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).filter(status=1, editor_reviewed=1)
    
    def resolve_last_month_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30)).filter(status=1, editor_reviewed=1)
    

    def resolve_post_by_category(self, info, category_uId, category_id = None, first=None, skip=None, **kwargs):
        category_id = kwargs.get('id')
        pk = kwargs.get('pk')
        category_uId = kwargs.get('uniqueId')

        if category_uId is not None:
            posts = Post.objects.filter(category__uniqueId=category_uId).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        elif category_id is not None:
            posts = Post.objects.filter(category_id=category_id).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        elif pk is not None:
            posts = Post.objects.filter(category_id=pk).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        else:
            return None

    def resolve_post_by_sub_category(self, info, sub_category_uId, sub_category_id = None, first=None, skip=None, **kwargs):
        sub_category_id = kwargs.get('id')
        pk = kwargs.get('pk')
        sub_category_uId = kwargs.get('uniqueId')

        if sub_category_uId is not None:
            posts = Post.objects.filter(sub_category__uniqueId=sub_category_uId).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        elif sub_category_id is not None:
            posts = Post.objects.filter(sub_category_id=sub_category_id).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        elif pk is not None:
            posts = Post.objects.filter(sub_category_id=pk).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        else:
            return None
        


    
    
    


#

class Mutation(graphene.ObjectType):
    pass
    # create_post = CreatePost.Field()
    # update_post = UpdatePost.Field()
    # delete_post = DeletePost.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
