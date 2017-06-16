import logging
import graphene
from .. import api_access
import json
from ..model.error_schema import ErrorsSchema



class CreateInstallationMutation(graphene.Mutation):

    def __init__(self, context, inputDict):
        self.schemaDict = {}
        self.http_status = None
        self.http_cause = None
        self.http_cause_is_json = False

        status, content = api_access.post_installations(x_user_agent = context['x_user_agent'], 
        	secureToken = inputDict['secureToken'], 
        	timestamp = inputDict['timestamp'], 
        	installationId = inputDict['installationId'], 
        	deviceId = inputDict['deviceId'] )
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
	        deviceId = graphene.String(required=True)
	        secureToken = graphene.String(required=True)
	        timestamp = graphene.String(required=True)

    installationId = graphene.String() 
    def resolve_installationId(self, args, context, info):
        return self.schemaDict.get('installationID')

    installationToken = graphene.String() 
    def resolve_installationToken(self, args, context, info):
        return self.schemaDict.get('installationToken')

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)
    
   
    def mutate(self, input, context, info):
        input_dict = {'installationId' : input.get('installationId'), 'deviceId' : input.get('deviceId'), 'secureToken' : input.get('secureToken'), 'timestamp' : input.get('timestamp') }   
        return CreateInstallationMutation(context, input_dict)