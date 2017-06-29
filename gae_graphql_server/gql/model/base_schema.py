import logging
import graphene
from .. import api_access
import json

class BaseApiInvokingSchema(graphene.ObjectType):


    def __init__(self, service_urls, x_user_agent, auth_token, fetch_func = None):
        self.schemaDict = {}
        self.http_status = None
        self.http_cause = None
        self.http_cause_is_json = False

        if fetch_func:
            status, content = fetch_func(service_urls, auth_token, x_user_agent)
            if status == 200:
                self.schemaDict = json.loads(content)
            else:
                #error
                self.http_status = status
                try:
                    self.http_cause = json.loads(content)
                    self.http_cause_is_json = True
                except:
                    self.http_cause = content