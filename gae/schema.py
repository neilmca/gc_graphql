from google.appengine.ext import ndb
import logging
import graphene
from graphene import relay, resolve_only_args
import api_access
import json








class ErrorsSchema(graphene.ObjectType):

    def __init__(self, status, cause):
        self.status = status
        self.cause = cause

    status = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_status')
        return self.status

    cause = graphene.String() 
    def resolve_cause(self, args, context, info):
        #logging.info('resolve_cause')
        return self.cause


class MeProfileInstallationSchema(graphene.ObjectType):

    def __init__(self, installation_json):
        self.json_object = installation_json
        #logging.info('MeProfileInstallationSchema.__init__ json_object = %s' % self.json_object )
       

    uuid = graphene.String() 
    def resolve_uuid(self, args, context, info):
        #logging.info('resolve_uuid = %s', self.json_object['uuid'])
        return self.json_object['uuid']

    identityId = graphene.String() 
    def resolve_identityId(self, args, context, info):
        #logging.info('resolve_identityId')
        return self.json_object['identityId']

class MeProfileIdentitySchema(graphene.ObjectType):

    def __init__(self, identity_json):
        self.json_object = identity_json
        
       

    id = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_id')
        return self.json_object['id']

    provider = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_provider')
        return self.json_object['provider']  

    firstName = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_firstName')
        return self.json_object['firstName']

    lastName = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_lastName')
        return self.json_object['lastName']

class MeProfileSchema(graphene.ObjectType):

    def __init__(self, context):
        self.me_profile_api_resp_json = None
        self.installation = None
        self.identities = None
        self.http_status = None
        self.http_cause = None

        status, content = api_access.get_me_profile(auth_token = context['auth_token'], x_user_agent = context['x_user_agent'])
        if status == 200:
            self.me_profile_api_resp_json = json.loads(content)
        else:
            #error
            self.http_status = status
            self.http_cause = content   
       

    userUid = graphene.String() 
    def resolve_userUid(self, args, context, info):        
        #logging.info('resolve_userUid = %s' % self.me_profile_api_resp_json)
        return self.me_profile_api_resp_json['userUid']

    installation = graphene.Field(MeProfileInstallationSchema) 
    def resolve_installation(self, args, context, info):        
        #logging.info('resolve_installation = %s' % self.me_profile_api_resp_json['installation'])
        return MeProfileInstallationSchema(self.me_profile_api_resp_json['installation'])


    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause)

class MeSchema(graphene.ObjectType):

    #profile 
    profile = graphene.Field(MeProfileSchema)
    def resolve_profile(self, args, context, info):
        #logging.info('resolve_profile')
        return MeProfileSchema(context)
    

class Query(graphene.ObjectType):
	
    #field authToken
    authToken = graphene.String() 
    def resolve_authToken(self, args, context, info):
        #logging.info('resolve_auth_token')
        return context['auth_token']


    #field xUsergAgent
    xUserAgent = graphene.String() 
    def resolve_xUserAgent(self, args, context, info):
        #logging.info('resolve_xUserAgent')
        return context['x_user_agent']
       
    #me 
    me = graphene.Field(MeSchema)
    def resolve_me(self, args, context, info):
        #logging.info('resolve_me')
        return MeSchema(context)

    





class GraphQlSchemaSingleton:
    instance = None

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
    	logging.info('initializing graphene schema singleton')
        self.schema = graphene.Schema(query=Query)       # or whatever you want to do



    


