import logging
import graphene
import api_access
import json

class BaseApiInvokingMutation(graphene.Mutation):


    def __init__(self, context, fetch_func = None):
        self.schemaDict = {}
        self.http_status = None
        self.http_cause = None
        self.http_cause_is_json = False

        