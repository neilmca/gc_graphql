import logging
import graphene

from mesubscriptions_schema import MeSubscriptionsSchema
from mefollowedplaylists_schema import MeFollowedPlaylistsSchema
from meprofile_schema import MeProfileSchema
from meaccountcheck_schema import MeAccountCheckSchema
from ..helpers.service_urls_helper import Helpers


class MeSchema(graphene.ObjectType):

    #profile 
    profile = graphene.Field(MeProfileSchema, authToken=graphene.Argument(graphene.String, required=True))
    def resolve_profile(self, args, context, info):
       
        return MeProfileSchema(Helpers.get_service_urls(context), context['x_user_agent'], args.get('authToken'))

    #subscriptions 
    subscriptions = graphene.Field(MeSubscriptionsSchema, authToken=graphene.Argument(graphene.String, required=True))
    def resolve_subscriptions(self, args, context, info):
        return MeSubscriptionsSchema(Helpers.get_service_urls(context), context['x_user_agent'], args.get('authToken'))

    #followedPlaylists 
    followedPlaylists = graphene.Field(MeFollowedPlaylistsSchema, authToken=graphene.Argument(graphene.String, required=True))
    def resolve_followedPlaylists(self, args, context, info):
        return MeFollowedPlaylistsSchema(Helpers.get_service_urls(context), context['x_user_agent'], args.get('authToken'))

    #acc_check
    accountCheck = graphene.Field(MeAccountCheckSchema, user_token = graphene.String(required=True), timestamp = graphene.String(required=True), user_name = graphene.String(required=True), device_uid = graphene.String(required=True))
    def resolve_accountCheck(self, args, context, info):
        return MeAccountCheckSchema(Helpers.get_service_urls(context), x_user_agent=context['x_user_agent'], user_token=args.get('user_token'), timestamp=args.get('timestamp'), user_name=args.get('user_name'), device_uid=args.get('device_uid'))