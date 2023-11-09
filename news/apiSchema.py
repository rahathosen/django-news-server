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
    last_week_popular_post  = graphene.List(PostType, first = graphene.Int(), skip = graphene.Int())
    last_month_popular_post = graphene.List(PostType, first = graphene.Int(), skip = graphene.Int())
   
    post_by_category = graphene.List(PostType, categoryuId = graphene.String(), first= graphene.Int(), skip = graphene.Int())
    last_10_post_by_category = graphene.List(PostType, categoryuId = graphene.String()) 
    last_10_post_by_sub_category = graphene.List(PostType, subCategoryuId = graphene.String())
    top_10_post_by_category_this_week = graphene.List(PostType, categoryuId = graphene.String())
    top_10_post_by_sub_category_this_week = graphene.List(PostType, subCategoryuId = graphene.String())

    post_by_sub_category = graphene.List(PostType, subCategoryuId = graphene.String(), first= graphene.Int(), skip = graphene.Int())
    last_10_post_by_sub_category = graphene.List(PostType, subCategoryuId = graphene.String())
    top_10_post_by_sub_category_this_week = graphene.List(PostType, subCategoryuId = graphene.String())

    post_by_tag = graphene.List(PostType, taguId = graphene.String(), first= graphene.Int(), skip = graphene.Int())
    last_10_post_by_tag = graphene.List(PostType, taguId = graphene.String())
    top_10_post_by_tag_this_week = graphene.List(PostType, taguId = graphene.String())

    
    

    
    def resolve_post(self, info, uId, id = None, **kwargs):
        id = kwargs.get('id')

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
        
        else:
            return None
        
    def resolve_all_posts(self, info, first, skip, **kwargs):
        posts =  Post.objects.all().filter(status=1, editor_reviewed=1)
        for post in posts:
            post.image.name = remove_file_extension(post.image.name)
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]
        return posts

    def resolve_last_week_popular_post(self, info, first, skip, **kwargs):
        posts = Post.objects.filter(status=1, editor_reviewed=1).filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by('-total_view')
        for post in posts:
            post.image.name = remove_file_extension(post.image.name)
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]
        return posts
    
    def resolve_last_month_popular_post(self, info, first, skip, **kwargs):
        posts = Post.objects.filter(status=1, editor_reviewed=1).filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30)).order_by('-total_view')
        for post in posts:
            post.image.name = remove_file_extension(post.image.name)
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]
        return posts

    def resolve_post_by_category(self, info, categoryuId,  first=None, skip=None, **kwargs):
     
        if categoryuId is not None:
            posts = Post.objects.filter(category__uniqueId=categoryuId).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        else:
            return None
        
    def resolve_last_10_post_by_category(self, info, categoryuId, **kwargs):
        if categoryuId is not None:
            posts = Post.objects.filter(category__uniqueId=categoryuId).filter(status=1, editor_reviewed=1)[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None
    
    def resolve_last_10_post_by_sub_category(self, info, subCategoryuId, **kwargs):
        if subCategoryuId is not None:
            posts = Post.objects.filter(subCategory__uniqueId=subCategoryuId).filter(status=1, editor_reviewed=1)[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None
    
    def resolve_top_10_post_by_category_this_week(self, info, categoryuId, **kwargs):
        if categoryuId is not None:
            posts = Post.objects.filter(category__uniqueId=categoryuId).filter(status=1, editor_reviewed=1).order_by('-total_view')[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None
    
    def resolve_top_10_post_by_sub_category_this_week(self, info, subCategoryuId, **kwargs):
        if subCategoryuId is not None:
            posts = Post.objects.filter(subCategory__uniqueId=subCategoryuId).filter(status=1, editor_reviewed=1).order_by('-total_view')[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None
    
    def resolve_post_by_sub_category(self, info, subCategoryuId,  first=None, skip=None, **kwargs):
         
        if subCategoryuId is not None:
            posts = Post.objects.filter(subCategory__uniqueId=subCategoryuId).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        else:
            return None
    
    def resolve_post_by_tag(self, info, taguId,  first=None, skip=None, **kwargs):
            
        if taguId is not None:
            posts = Post.objects.filter(tag__uniqueId=taguId).filter(status=1, editor_reviewed=1)
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            if skip:
                posts = posts[skip:]
            if first:
                posts = posts[:first]
            return posts
        
        else:
            return None
        
    def resolve_last_10_post_by_tag(self, info, taguId, **kwargs):
        if taguId is not None:
            posts = Post.objects.filter(tag__uniqueId=taguId).filter(status=1, editor_reviewed=1)[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None
    
    def resolve_top_10_post_by_tag_this_week(self, info, taguId, **kwargs):
        if taguId is not None:
            posts = Post.objects.filter(tag__uniqueId=taguId).filter(status=1, editor_reviewed=1).order_by('-total_view')[:10]
            for post in posts:
                post.image.name = remove_file_extension(post.image.name)
            return posts
        
        else:
            return None


    




class Mutation(graphene.ObjectType):
    pass
    # create_post = CreatePost.Field()
    # update_post = UpdatePost.Field()
    # delete_post = DeletePost.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
