
import logging
import graphene
from .. import api_access
import json
from base_schema import BaseApiInvokingSchema
from error_schema import ErrorsSchema
from playlistfeeditem_schema import PlaylistFeedItemSchema

class MeFollowedPlaylistsSchema(BaseApiInvokingSchema):

    def __init__(self, service_urls, x_user_agent, auth_token):
        BaseApiInvokingSchema.__init__(self, service_urls, x_user_agent, auth_token)  # don't get base class to call API as we need to do two API calls

        #get followed playlists
        status, content = api_access.get_me_follows(service_urls, auth_token, x_user_agent)
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

        #get playlist details
        playlistIds = self.schemaDict.get('followedPlaylistFeeds')
        self.playlist_feed_details_dict = {}
        if playlistIds:
            status, content = api_access.get_playlist_feeds(service_urls, auth_token, x_user_agent, playlistIds)
            if status == 200:
                self.playlist_feed_details_dict = json.loads(content)
            else:
                #error
                self.http_status = status
                try:
                    self.http_cause = json.loads(content)
                    self.http_cause_is_json = True
                except:
                    self.http_cause = content 



    followedPlaylistFeedsPrepopulated = graphene.String()
    def resolve_followedPlaylistFeedsPrepopulated(self, args, context, info):        
        return self.schemaDict.get('followedPlaylistFeedsPrepopulated')  

    
    followedPlaylistFeedIds = graphene.List(graphene.String) 
    def resolve_followedPlaylistFeedIds(self, args, context, info):              
        return self.schemaDict.get('followedPlaylistFeeds')

    followedPlaylistFeeds = graphene.List(PlaylistFeedItemSchema) 
    def resolve_followedPlaylistFeeds(self, args, context, info):      

        feeds_schema = []
        if self.playlist_feed_details_dict:
            for feed in self.playlist_feed_details_dict:
                feeds_schema.append(PlaylistFeedItemSchema(feed))
        return feeds_schema       

    errors = graphene.Field(ErrorsSchema) 
    def resolve_errors(self, args, context, info):
        #logging.info('resolve_errors')
        return ErrorsSchema(self.http_status, self.http_cause, self.http_cause_is_json)