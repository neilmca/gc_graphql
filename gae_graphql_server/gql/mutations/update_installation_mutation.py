import logging
import graphene
from .. import api_access
import json
from ..model.error_schema import ErrorsSchema
from ..helpers.service_urls_helper import Helpers



class UpdateInstallationMutation(graphene.Mutation):

    def __init__(self, service_urls, x_user_agent, inputDict):
        self.schemaDict = {}
        self.http_status = None
        self.http_cause = None
        self.http_cause_is_json = False

        status, content = api_access.put_installations(service_urls, x_user_agent = x_user_agent, 
        	secureToken = inputDict['secureToken'], 
        	timestamp = inputDict['timestamp'], 
        	installationId = inputDict['installationId'], 
            social_type =  inputDict['socialType'],
            social_access_token =  inputDict['socialAccessToken'],
            social_email =  inputDict['socialEmail'],
            social_id =  inputDict['socialId'],)
        if status == 200 or status == 201:
            self.schemaDict = json.loads(content)
        else:
            #error
            self.http_status = status
            try:
                self.http_cause = json.loads(content)
                self.http_cause_is_json = True
            except:
                self.http_cause = content

    class Input:
        installationId = graphene.String(required=True)
        secureToken = graphene.String(required=True)
        timestamp = graphene.String(required=True)
        socialType = graphene.String(required=True) 
        socialAccessToken = graphene.String(required=True)
        socialEmail = graphene.String(required=True)
        socialId = graphene.String(required=True)

    userId = graphene.String() 
    def resolve_userId(self, args, context, info):
        return self.schemaDict.get('userId')

    installationToken = graphene.String() 
    def resolve_installationToken(self, args, context, info):
        return self.schemaDict.get('installationToken')

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)
    
   
    def mutate(self, input, context, info):
        input_dict = {'installationId' : input.get('installationId'), 
                        'secureToken' : input.get('secureToken'), 
                        'timestamp' : input.get('timestamp'), 
                        'socialType' : input.get('socialType'), 
                        'socialAccessToken' : input.get('socialAccessToken'), 
                        'socialEmail' : input.get('socialEmail'),
                        'socialId' : input.get('socialId')  }   
        return UpdateInstallationMutation(Helpers.get_service_urls(context), context['x_user_agent'], input_dict)