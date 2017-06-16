import logging
import graphene
import json

def json_dump(str):
    return json.dumps(str)

class ErrorsSchema(graphene.ObjectType):

    def __init__(self, status, cause, cause_is_json):
        self.status = status
        self.cause = cause
        self.cause_is_json = cause_is_json

    status = graphene.String() 
    def resolve_status(self, args, context, info):
        #logging.info('resolve_status')
        return self.status

    cause = graphene.String() 
    def resolve_cause(self, args, context, info):
        #logging.info('resolve_cause')
        if self.cause_is_json:
            return json_dump(self.cause)
        else:
            return self.cause



    