import logging
import graphene


class MeSubscriptionsTiersItemSchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}

    level = graphene.String() 
    def resolve_level(self, args, context, info):
        return self.schemaDict.get('level')

    validFrom = graphene.String() 
    def resolve_validFrom(self, args, context, info):
        return self.schemaDict.get('validFrom')