from google.appengine.api import users
import webapp2
import logging
import base64
import string
import re
import json

from collections import OrderedDict
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

        
        
        self.response.write(json.dumps(GraphQlSchemaSingleton.get().schema.introspect()))

    def post(self):
        #execute the requested query

        
        

        #get x-user-agent
        x_user_agent = self.request.headers.get('X-User-Agent')
        if x_user_agent == None:
            logging.info('WARNING - no x_user_agent provided')

        #get core_server_url
        core_server_url = self.request.headers.get('core_server_url')        
        if core_server_url == None:
            logging.info('WARNING - no core_server_url provided')

        #get pls_server_url
        pls_server_url = self.request.headers.get('pls_server_url')        
        if pls_server_url == None:
            logging.info('WARNING - no pls_server_url provided')




        ctx_value = {'x_user_agent': x_user_agent, 'pls_server_url' : pls_server_url, 'core_server_url': core_server_url}


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




