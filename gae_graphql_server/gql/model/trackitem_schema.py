import logging
import graphene

class TrackItemSchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}

    id = graphene.String() 
    def resolve_title(self, args, context, info):
        return self.schemaDict.get('id')

    title = graphene.String() 
    def resolve_id(self, args, context, info):
        return self.schemaDict.get('title')

    artist = graphene.String() 
    def resolve_artist(self, args, context, info):
        return self.schemaDict.get('artist')

    isrc = graphene.String() 
    def resolve_isrc(self, args, context, info):
        return self.schemaDict.get('isrc')