import graphene
from graphene_django import DjangoObjectType

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
    ad_boxes = graphene.List(AdBoxType, first = graphene.Int(), skip = graphene.Int())
    ad_box = graphene.List(AdBoxType, uId=graphene.String())
    ad_companies = graphene.List(AdCompanyType, first = graphene.Int(), skip = graphene.Int())
    ad_company = graphene.Field(AdCompanyType, uId=graphene.String())
    advertisements = graphene.List(AdvertisementType, first = graphene.Int(), skip = graphene.Int())
    advertisement = graphene.Field(AdvertisementType, uId=graphene.String())
    ads_by_box = graphene.Field(AdvertisementType, uId=graphene.String())

    def resolve_ad_boxes(self, info, first=None, skip=None, **kwargs):
        ad_boxes = AdBox.objects.all()
        if skip:
            ad_boxes = ad_boxes[skip:]
        if first:
            ad_boxes = ad_boxes[:first]

        return ad_boxes
    
    def resolve_ad_box(self, uId, info, **kwargs):
        
        if uId is not None:
            obj = AdBox.objects.get(uniqueId=uId)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
       
        else:
            return None
    
    def resolve_ad_companies(self, info, first=None, skip=None, **kwargs):
        ad_companies = AdCompany.objects.all()
        if skip:
            ad_companies = ad_companies[skip:]
        if first:
            ad_companies = ad_companies[:first]

        return ad_companies
    
    def resolve_ad_company(self, uId, info, **kwargs):
        id = kwargs.get('id')
        
        if uId is not None:
            obj = AdCompany.objects.get(uniqueId=uId)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        elif id is not None:
            obj = AdCompany.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        else:
            return None
    
    def resolve_advertisements(self, info, first=None, skip=None, **kwargs):
        advertisements = Advertisement.objects.all()
        if skip:
            advertisements = advertisements[skip:]
        if first:
            advertisements = advertisements[:first]

        return advertisements
    
    def resolve_advertisement(self, uId, info, **kwargs):
        id = kwargs.get('id')

        if uId is not None:
            obj = Advertisement.objects.get(uniqueId=uId)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        elif id is not None:
            obj = Advertisement.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        else:
            return None
        
    def resolve_ads_by_box(self, uId, info, **kwargs):
        if uId is not None:
            obj = Advertisement.objects.get(addBox__uniqueId=uId)
            return obj
        else:
            return None
    
class Mutation(graphene.ObjectType):
    pass
    
schema = graphene.Schema(query=Query, mutation=Mutation)
