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

# query adBoxesQuery {
#   adBoxes {
#     uniqueId
#     position
#     size
#     active
#   }
# }

# {
#   "data": {
#     "adBoxes": [
#       {
#         "uniqueId": "Leaderboard728X90",
#         "position": "Leaderboard 728×90",
#         "size": "728X90",
#         "active": "A_1"
#       },
#       {
#         "uniqueId": "Rectangle366X280",
#         "position": "Rectangle 366 × 280 px",
#         "size": "Rectangle 366 × 280 px",
#         "active": "A_1"
#       },
#       {
#         "uniqueId": "Medium300X250",
#         "position": "Medium Rectangle-300 × 250 px",
#         "size": "Medium Rectangle-300 × 250 px",
#         "active": "A_1"
#       }
#     ]
#   }
# }

# query adsByBoxQuery {
#   adsByBox(boxuId: "Leaderboard728X90") {
#     image
#     link
#     status
#     stopAt
#     totalView
#   }
# }