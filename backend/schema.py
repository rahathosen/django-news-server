import graphene
import webInfo.apiSchema
import advertisement.apiSchema
import article.apiSchema
import categories.apiSchema
import feature.apiSchema
import news.apiSchema
import reporter.apiSchema
import search.apiSchema
    
class Query(

    # Add your Query objects here
    webInfo.apiSchema.Query,
    advertisement.apiSchema.Query,
    article.apiSchema.Query,
    categories.apiSchema.Query,
    feature.apiSchema.Query,
    news.apiSchema.Query,
    reporter.apiSchema.Query,
    search.apiSchema.Query,
    
    graphene.ObjectType
):
    pass

class Mutation(
    # Add your Mutation objects here
    advertisement.apiSchema.Mutation,
    article.apiSchema.Mutation,
    categories.apiSchema.Mutation,
    news.apiSchema.Mutation,
    webInfo.apiSchema.Mutation,
    reporter.apiSchema.Mutation,
    feature.apiSchema.Mutation,
    
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