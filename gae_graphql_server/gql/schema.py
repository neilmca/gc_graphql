import logging
import graphene
from model.me_schema import MeSchema
from mutations.create_installation_mutation import CreateInstallationMutation
from mutations.update_installation_mutation import UpdateInstallationMutation


    

class Queries(graphene.ObjectType):
	
    #field authToken
    authToken = graphene.String() 
    def resolve_authToken(self, args, context, info):
        #logging.info('resolve_auth_token')
        return context['auth_token']


    #field xUsergAgent
    xUserAgent = graphene.String() 
    def resolve_xUserAgent(self, args, context, info):
        #logging.info('resolve_xUserAgent')
        return context['x_user_agent']
       
    #me 
    me = graphene.Field(MeSchema)
    def resolve_me(self, args, context, info):
        #logging.info('resolve_me')
        return MeSchema(context)



class Mutations(graphene.ObjectType):
    createInstallation = CreateInstallationMutation.Field()
    updateInstallation = UpdateInstallationMutation.Field()
    





class GraphQlSchemaSingleton:
    instance = None

    @classmethod
    def get(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
    	logging.info('initializing graphene schema singleton')
        self.schema = graphene.Schema(query=Queries, mutation = Mutations)       # or whatever you want to do



    



