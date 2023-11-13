import datetime
import graphene
from graphene_django import DjangoObjectType

from feature.models import Feature, FeatureCategory, FeaturePost

class FeatureType(DjangoObjectType):
    class Meta:
        model = Feature
        fields = "__all__"

class FeatureCategoryType(DjangoObjectType):
    class Meta:
        model = FeatureCategory
        fields = "__all__"

class FeaturePostType(DjangoObjectType):
    class Meta:
        model = FeaturePost
        fields = "__all__"

class Query(graphene.ObjectType):
    all_feature = graphene.List(FeatureType)
    feature = graphene.Field(FeatureType, featureId = graphene.String())
    featuer_category_by_featuerUID = graphene.List(FeatureCategoryType, featureUId = graphene.String())
    feature_post_by_category = graphene.List(FeaturePostType, categoryuId = graphene.String())
    feature_posts = graphene.List(FeaturePostType)
    feature_post = graphene.Field(FeaturePostType, featurePostuId = graphene.String())

    def resolve_all_feature(self, info, **kwargs):
        return Feature.objects.all().filter(status=1)
    
    def resolve_feature(self, info, featureId, **kwargs):
        return Feature.objects.get(uniqueId=featureId, status=1)
    
    def resolve_featuer_category_by_featuerUID(self, info, featureUId, **kwargs):
        return FeatureCategory.objects.filter(feature__uniqueId=featureUId, status=1)
    
    def resolve_feature_post_by_category(self, info, categoryuId, **kwargs):
        return FeaturePost.objects.filter(category__uniqueId=categoryuId, status=1)
    
    def resolve_feature_posts(self, info, **kwargs):
        return FeaturePost.objects.all().filter(status=1)
    
    def resolve_feature_post(self, info, featurePostuId, **kwargs):
        return FeaturePost.objects.get(uniqueId=featurePostuId, status=1)
    

    
class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)