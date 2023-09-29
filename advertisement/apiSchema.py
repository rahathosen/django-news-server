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
    ad_box = graphene.Field(AdBoxType, id=graphene.Int())
    ad_companies = graphene.List(AdCompanyType, first = graphene.Int(), skip = graphene.Int())
    ad_company = graphene.Field(AdCompanyType, id=graphene.Int())
    advertisements = graphene.List(AdvertisementType, first = graphene.Int(), skip = graphene.Int())
    advertisement = graphene.Field(AdvertisementType, id=graphene.Int())

    def resolve_ad_boxes(self, info, first=None, skip=None, **kwargs):
        ad_boxes = AdBox.objects.all()
        if skip:
            ad_boxes = ad_boxes[skip:]
        if first:
            ad_boxes = ad_boxes[:first]

        return ad_boxes
    
    def resolve_ad_box(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = AdBox.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_ad_companies(self, info, first=None, skip=None, **kwargs):
        ad_companies = AdCompany.objects.all()
        if skip:
            ad_companies = ad_companies[skip:]
        if first:
            ad_companies = ad_companies[:first]

        return ad_companies
    
    def resolve_ad_company(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = AdCompany.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_advertisements(self, info, first=None, skip=None, **kwargs):
        advertisements = Advertisement.objects.all()
        if skip:
            advertisements = advertisements[skip:]
        if first:
            advertisements = advertisements[:first]

        return advertisements
    
    def resolve_advertisement(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Advertisement.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
schema = graphene.Schema(query=Query)
