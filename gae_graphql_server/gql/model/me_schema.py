import logging
import graphene

from mesubscriptions_schema import MeSubscriptionsSchema
from mefollowedplaylists_schema import MeFollowedPlaylistsSchema
from meprofile_schema import MeProfileSchema


class MeSchema(graphene.ObjectType):

    #profile 
    profile = graphene.Field(MeProfileSchema)
    def resolve_profile(self, args, context, info):
        #logging.info('resolve_profile')
        return MeProfileSchema(context)

    #subscriptions 
    subscriptions = graphene.Field(MeSubscriptionsSchema)
    def resolve_subscriptions(self, args, context, info):
        return MeSubscriptionsSchema(context)

    #followedPlaylists 
    followedPlaylists = graphene.Field(MeFollowedPlaylistsSchema)
    def resolve_followedPlaylists(self, args, context, info):
        return MeFollowedPlaylistsSchema(context)