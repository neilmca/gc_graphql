import logging
import graphene
from trackitem_schema import TrackItemSchema

class PlaylistInstanceSchema(graphene.ObjectType):

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

    subtitle = graphene.String() 
    def resolve_subtitle(self, args, context, info):
        return self.schemaDict.get('subtitle')

    description = graphene.String() 
    def resolve_description(self, args, context, info):
        return self.schemaDict.get('description')

    servingUrl = graphene.String() 
    def resolve_servingUrl(self, args, context, info):
        return self.schemaDict.get('servingUrl')

    tracks = graphene.List(TrackItemSchema) 
    def resolve_tracks(self, args, context, info):  
        items = []
        if 'tracks' in self.schemaDict:
	        for item in self.schemaDict['tracks']:
	            items.append(TrackItemSchema(item))
        return items  



