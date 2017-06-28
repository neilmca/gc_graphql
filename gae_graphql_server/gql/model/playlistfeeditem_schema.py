import logging
import graphene
from playlistinstance_schema import PlaylistInstanceSchema

class PlaylistFeedItemSchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}

    id = graphene.String() 
    def resolve_id(self, args, context, info):
        return self.schemaDict.get('id')

    title = graphene.String() 
    def resolve_title(self, args, context, info):
        return self.schemaDict.get('title')

    description = graphene.String() 
    def resolve_description(self, args, context, info):
        return self.schemaDict.get('description')

    instance = graphene.Field(PlaylistInstanceSchema) 
    def resolve_instance(self, args, context, info):      
        return PlaylistInstanceSchema(self.schemaDict.get('instance'))