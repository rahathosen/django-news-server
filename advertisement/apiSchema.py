import graphene
from graphene_django import DjangoObjectType
from datetime import *
from django.utils import timezone
from advertisement.models import AdBox, AdCompany, Advertisement

class AdBoxType(DjangoObjectType):
    class Meta:
        model = AdBox
        fields = "__all__"

class AdCompanyType(DjangoObjectType):
    class Meta:
        model = AdCompany
        fields = "__all__"

class AdvertisementType(DjangoObjectType):
    class Meta:
        model = Advertisement
        fields = "__all__"

class Query(graphene.ObjectType):
    ad_boxes = graphene.List(AdBoxType)
    ads_by_Box = graphene.Field(AdvertisementType, boxuId=graphene.String())
    ads_by_Box_position = graphene.Field(AdvertisementType, boxPosition=graphene.Int())
    all_ads = graphene.List(AdvertisementType)

    def resolve_ad_boxes(self, info,**kwargs):
        return AdBox.objects.all()
    
    def resolve_ads_by_Box_position(self, info, boxPosition, **kwargs):
        obj = Advertisement.objects.filter(addBox__box_position_id=boxPosition, status=1).first()
        print(obj.stop_at)
        print(timezone.now())
        if obj.stop_at > timezone.now():
            obj.total_view += 1
            obj.save()
            return obj
        return None
    
    def resolve_all_ads(self, info, **kwargs):
        return Advertisement.objects.all()
    
class Mutation(graphene.ObjectType):
    pass
    
schema = graphene.Schema(query=Query, mutation=Mutation)