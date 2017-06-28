import logging
import graphene
from .. import api_access
from base_schema import BaseApiInvokingSchema
from error_schema import ErrorsSchema
import json



class MeAccountCheckSchema(BaseApiInvokingSchema):

    def __init__(self, context, user_token, timestamp, user_name, device_uid):
        BaseApiInvokingSchema.__init__(self, context, None)     

        
        status, content = api_access.get_acc_check(user_token = user_token, x_user_agent = context['x_user_agent'], timestamp = timestamp, user_name = user_name, device_uid = device_uid)
        if status == 200:
             resp = json.loads(content)
             resp = resp.get('response')
             data = resp.get('data')
             user_outer = data[0]
             user = user_outer.get('user')
             self.schemaDict = user
        else:
            #error
            self.http_status = status
            try:
                self.http_cause = json.loads(content)
                self.http_cause_is_json = True
            except:
                self.http_cause = content

        


    rememberMeToken = graphene.String() 
    def resolve_rememberMeToken(self, args, context, info):        
        #logging.info('resolve_userUid = %s' % self.schemaDict)
        return self.schemaDict.get('rememberMeToken')

    

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)