import graphene

class Query(graphene.ObjectType):
	#field hello
    hello = graphene.String(name=graphene.Argument(graphene.String, default_value="stranger"))    

    def resolve_hello(self, args, context, info):
    	logging.info('resolve_hello')
        return 'Hello ' + args['name']


schema = graphene.Schema(query=Query)