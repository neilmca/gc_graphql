import logging
import graphene
from .. import api_access
from base_schema import BaseApiInvokingSchema
from meprofileinstallation_schema import MeProfileInstallationSchema
from meprofileidentity_schema import MeProfileIdentitySchema
from error_schema import ErrorsSchema


class MeProfileSchema(BaseApiInvokingSchema):

    def __init__(self, service_urls, x_user_agent, authToken):
        BaseApiInvokingSchema.__init__(self, service_urls, x_user_agent, authToken, api_access.get_me_profile)     

    userUid = graphene.String() 
    def resolve_userUid(self, args, context, info):        
        #logging.info('resolve_userUid = %s' % self.schemaDict)
        return self.schemaDict.get('userUid')

    installation = graphene.Field(MeProfileInstallationSchema) 
    def resolve_installation(self, args, context, info):        
        #logging.info('resolve_installation = %s' % self.me_profile_api_resp_json['installation'])
        return MeProfileInstallationSchema(self.schemaDict.get('installation'))

    identities = graphene.List(MeProfileIdentitySchema) 
    def resolve_identities(self, args, context, info):        
        #logging.info('resolve_identities = %s' % self.me_profile_api_resp_json['identities'])
        
        identities_schema = []
        if 'identities' in self.schemaDict:
            for i in self.schemaDict.get('identities'):
                identities_schema.append(MeProfileIdentitySchema(i))
        return identities_schema

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)
        