import logging
import graphene

from mesubscriptions_schema import MeSubscriptionsSchema
from mefollowedplaylists_schema import MeFollowedPlaylistsSchema
from meprofile_schema import MeProfileSchema
from meaccountcheck_schema import MeAccountCheckSchema


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

    #acc_check
    accountCheck = graphene.Field(MeAccountCheckSchema, user_token = graphene.String(required=True), timestamp = graphene.String(required=True), user_name = graphene.String(required=True), device_uid = graphene.String(required=True))
    def resolve_accountCheck(self, args, context, info):
        return MeAccountCheckSchema(context=context, user_token=args.get('user_token'), timestamp=args.get('timestamp'), user_name=args.get('user_name'), device_uid=args.get('device_uid'))