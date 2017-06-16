from google.appengine.api import users
import webapp2
import logging
import base64
import string
import re
import json


from gql.schema import GraphQlSchemaSingleton
from gql.middleware import AuthorizationMiddleware

#grahpQL imports
import graphene







class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        # Log the error.
        
        logging.exception(exception)

        # Set a custom message.
        self.response.write('An error occurred.')

        # If the exception is a HTTPException, use its error code.
        # Otherwise use a generic 500 error code.
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)




class GraphQlApiGatewayHandler(BaseHandler):

   
    def get(self):

        #path param 1  = total number of vouchers to assign as "used"

        

        #E.g. http://localhost:8080assign=1000

        path = re.sub('^/', '', self.request.path)
        path = re.sub('/$', '', path)

                
        split = path.split('/')

        logging.info(split)
                 
        
                               

        self.response.write('ok')

    def post(self):
        #execute the requested query

        
        #get auth header
        auth_token = None
        AUTH_HEADER = 'Authorization'
        if AUTH_HEADER in self.request.headers:
            bearer_token = self.request.headers[AUTH_HEADER]
            
            if ' ' in bearer_token:
                param, auth_token = bearer_token.split(' ',1)


        if auth_token == None:
            logging.info('WARNING - no auth token provided')

        #get x-user-agent
        x_user_agent = ''
        X_USER_AGENT_HEADER = 'X-User-Agent'
        if X_USER_AGENT_HEADER in self.request.headers:
            x_user_agent = self.request.headers[X_USER_AGENT_HEADER]
        
        if x_user_agent == None:
            logging.info('WARNING - no x_user_agent provided')


        ctx_value = {'auth_token': auth_token, 'x_user_agent': x_user_agent}


        #result = GraphQlSchemaSingleton.get().schema.execute(self.request.body, middleware = [AuthorizationMiddleware()], context_value=ctx_value)
        result = GraphQlSchemaSingleton.get().schema.execute(self.request.body,  context_value=ctx_value)
        #logging.info(result)
        #logging.info(result.data)
        logging.info('graphQL errors = %s', result.errors)

        if result.errors != None:
            #error occured in execution
            self.response.set_status(400)
            self.response.write(result.errors)
            return
        

        ordered_list = [{key: val} for key, val in result.data.items()]
        js = json.dumps(ordered_list)
        self.response.write(js)





#logging.getLogger().setLevel(logging.DEBUG)

#logging.info('Serving Url = %s' % app_identity.get_default_version_hostname())

app = webapp2.WSGIApplication([
    ('/.*', GraphQlApiGatewayHandler)    
    
], debug=True)




