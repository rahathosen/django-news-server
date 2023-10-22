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
    all_feature_category = graphene.List(FeatureCategoryType)
    all_feature_post = graphene.List(FeaturePostType)

    featuer_category = graphene.Field(FeatureCategoryType, id=graphene.Int(), uniqueId = graphene.String())

    feature_post = graphene.Field(FeaturePostType, id=graphene.Int(), uniqueId = graphene.String())

    def resolve_all_feature(self, info, **kwargs):
        return Feature.objects.all()

    def resolve_all_feature_category(self, info, **kwargs):
        return FeatureCategory.objects.all()

    def resolve_all_feature_post(self, info, **kwargs):
        return FeaturePost.objects.all()
    
    def resolve_feature_category(self, info, uniqueId, **kwargs):
        id = kwargs.get('id')
        uniqueId = kwargs.get('uniqueId')

        if id is not None:
            return FeatureCategory.objects.get(pk=id)
        
        if uniqueId is not None:
            return FeatureCategory.objects.get(uniqueId=uniqueId)

        return None
    
    def resolve_feature_post(self, info, uniqueId, **kwargs):
        id = kwargs.get('id')
        uniqueId = kwargs.get('uniqueId')

        if id is not None:
            return FeaturePost.objects.get(pk=id)
        
        if uniqueId is not None:
            return FeaturePost.objects.get(uniqueId=uniqueId)

        return None

class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)