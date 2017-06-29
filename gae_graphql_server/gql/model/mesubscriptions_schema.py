import logging
import graphene
from .. import api_access
from base_schema import BaseApiInvokingSchema
from error_schema import ErrorsSchema
from mesubscriptiontier_schema import MeSubscriptionsTierSchema
from mesubscriptiontieritem_schema import MeSubscriptionsTiersItemSchema

class MeSubscriptionsSchema(BaseApiInvokingSchema):

    def __init__(self, service_urls, x_user_agent, authToken):
        BaseApiInvokingSchema.__init__(self, service_urls, x_user_agent, authToken, api_access.get_me_subscriptions)  

    serverTime = graphene.String()
    def resolve_serverTime(self, args, context, info):        
        #logging.info('resolve_userUid = %s' % self.schemaDict)
        return self.schemaDict.get('serverTime')

    tier = graphene.Field(MeSubscriptionsTierSchema) 
    def resolve_tier(self, args, context, info):        
        return MeSubscriptionsTierSchema(self.schemaDict.get('tier'))


    tiers = graphene.List(MeSubscriptionsTiersItemSchema) 
    def resolve_tiers(self, args, context, info):              
        tiers_schema = []
        if 'tiers' in self.schemaDict:
            for i in self.schemaDict.get('tiers'):
                tiers_schema.append(MeSubscriptionsTiersItemSchema(i))
        return tiers_schema

        

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)