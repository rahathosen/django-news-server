import datetime
import graphene
from graphene_django import DjangoObjectType

from news.models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class Query(graphene.ObjectType):
    post = graphene.Field(PostType, id=graphene.Int())
   
    today_posts = graphene.List(PostType)
    last_week_popular_post  = graphene.List(PostType)
    last_month_popular_post = graphene.List(PostType)

    post_by_category = graphene.List(PostType, category_id=graphene.Int())
    post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int())
    post_by_country = graphene.List(PostType, country_id=graphene.Int())
    post_by_division = graphene.List(PostType, division_id=graphene.Int())
    post_by_district = graphene.List(PostType, district_id=graphene.Int())
    post_by_cityCorporation = graphene.List(PostType, cityCorporation_id=graphene.Int())
    post_by_upozila = graphene.List(PostType, upozila_id=graphene.Int())
    post_by_zip_postal_code = graphene.List(PostType, zip_postal_code_id=graphene.Int())
    post_by_tag = graphene.List(PostType, tag_id=graphene.Int())
    post_by_reporter = graphene.List(PostType, author_id=graphene.Int())

    last_8_post_by_category = graphene.List(PostType, category_id=graphene.Int())
    last_8_post_by_sub_category = graphene.List(PostType, sub_category_id=graphene.Int())

    top_8_post_by_category_this_week = graphene.List(PostType, category_id=graphene.Int())
    top_8_post_by_sub_category_this_week = graphene.List(PostType, sub_category_id=graphene.Int())

    filter_post = graphene.List(PostType, category_id=graphene.Int(), sub_category_id=graphene.Int(), country_id=graphene.Int(), division_id=graphene.Int(), district_id=graphene.Int(), cityCorporation_id=graphene.Int(), upozila_id=graphene.Int(), zip_postal_code_id=graphene.Int(), tag_id=graphene.Int(), author_id=graphene.Int())

    
    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            obj = Post.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_posts(self, info, first=None, skip=None, **kwargs):
        posts = Post.objects.all()
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]

        return posts
    
    def resolve_today_posts(self, info, **kwargs):
        return Post.objects.filter(created_at__date=datetime.date.today()).order_by(total_view='DESC')
    
    def resolve_last_week_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by(total_view='DESC')
    
    def resolve_last_month_popular_post(self, info, **kwargs):
        return Post.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30)).order_by(total_view='DESC')
    

    def resolve_post_by_category(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_sub_category(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_country(self, info, country_id, **kwargs):
        return Post.objects.filter(country_id=country_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_division(self, info, division_id, **kwargs):
        return Post.objects.filter(division_id=division_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_district(self, info, district_id, **kwargs):
        return Post.objects.filter(district_id=district_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_cityCorporation(self, info, cityCorporation_id, **kwargs):
        return Post.objects.filter(cityCorporation_id=cityCorporation_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_upozila(self, info, upozila_id, **kwargs):
        return Post.objects.filter(upozila_id=upozila_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_zip_postal_code(self, info, zip_postal_code_id, **kwargs):
        return Post.objects.filter(zip_postal_code_id=zip_postal_code_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_tag(self, info, tag_id, **kwargs):
        return Post.objects.filter(tag_id=tag_id).ordered_by(created_at="-created_at")
    
    def resolve_post_by_reporter(self, info, author_id, **kwargs):
        return Post.objects.filter(author_id=author_id).ordered_by(created_at="-created_at")
    
    
    def resolve_last_8_post_by_category(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id).ordered_by(created_at="-created_at")[:8]
    
    def resolve_last_8_post_by_sub_category(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id).ordered_by(created_at="-created_at")[:8]
    
    
    def resolve_top_8_post_by_category_this_week(self, info, category_id, **kwargs):
        return Post.objects.filter(category_id=category_id, created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by(total_view='DESC')[:8]
        
    def resolve_top_8_post_by_sub_category_this_week(self, info, sub_category_id, **kwargs):
        return Post.objects.filter(sub_category_id=sub_category_id, created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by(total_view='DESC')[:8]
    
    def resolve_filter_post(self, info, category_id, sub_category_id, country_id, division_id, district_id, cityCorporation_id, upozila_id, zip_postal_code_id, tag_id, author_id, **kwargs):
        return Post.objects.filter(category_id=category_id, sub_category_id=sub_category_id, country_id=country_id, division_id=division_id, district_id=district_id, cityCorporation_id=cityCorporation_id, upozila_id=upozila_id, zip_postal_code_id=zip_postal_code_id, tag_id=tag_id, author_id=author_id).ordered_by(created_at="-created_at")

    
    
schema = graphene.Schema(query=Query)

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

