import logging
import graphene

class MeSubscriptionsTierSchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}

    level = graphene.String() 
    def resolve_level(self, args, context, info):
        #logging.info('resolve_level')
        return self.schemaDict.get('level')

