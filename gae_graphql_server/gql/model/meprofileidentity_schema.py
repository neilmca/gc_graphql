import logging
import graphene

class MeProfileIdentitySchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}  
       

    id = graphene.String() 
    def resolve_id(self, args, context, info):
        #logging.info('resolve_id')
        return self.schemaDict.get('id')

    provider = graphene.String() 
    def resolve_provider(self, args, context, info):
        #logging.info('resolve_provider')
        return self.schemaDict.get('provider')

    firstName = graphene.String() 
    def resolve_firstName(self, args, context, info):
        #logging.info('resolve_firstName')
        return self.schemaDict.get('firstName')

    lastName = graphene.String() 
    def resolve_lastName(self, args, context, info):
        #logging.info('resolve_lastName')
        return self.schemaDict.get('lastName')