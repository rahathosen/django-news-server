import graphene
import webInfo.apiSchema
import news.apiSchema

    
class Query(

    # Add your Query objects here
    webInfo.apiSchema.Query,
    news.apiSchema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    # Add your Mutation objects here
    webInfo.apiSchema.Mutation,
    graphene.ObjectType
):
    pass
    # token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.relay.Verify.Field()
    # refresh_token = graphql_jwt.relay.Refresh.Field()
    # delete_token_cookie = graphql_jwt.relay.DeleteJSONWebTokenCookie.Field()

    # # Long running refresh tokens
    # revoke_token = graphql_jwt.relay.Revoke.Field()

    # delete_refresh_token_cookie = \
    #     graphql_jwt.relay.DeleteRefreshTokenCookie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)