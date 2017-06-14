import graphene


	
class ServiceManifestSchema(graphene.ObjectType):

    def __init__(self, url):
		self.url = url
		self.name = ''
		self.version = ''
		print('__init__ %s' % self.url)

    url = graphene.String() 
    def resolve_url(self, args, context, info):
    	print('resolve_url %s' % self.url)
        return self.url


    name = graphene.String() 
    def resolve_name(self, args, context, info):
        return self.name

    version = graphene.String() 
    def resolve_version(self, args, context, info):
        return self.version
   
    

class Query(graphene.ObjectType):
	
    #field service manifest    
    
    servicemanifest = graphene.Field(ServiceManifestSchema, url=graphene.Argument(graphene.String, default_value="undefined"))
    

    def resolve_servicemanifest(self, args, context, info):
        print('resolve_servicemanifest %s' % args['url'])
        return ServiceManifestSchema(args['url'])


class LoggerMiddleware(object):
    def resolve(self, next, root, args, context, info):
    	print('AuthorizationMiddleware')
    	print('root=%s' % str(root))
    	print('args=%s' % str(args))
    	print('context=%s' % str(context))
    	print('info.field_name=%s' % str(info.field_name))

        #if info.field_name == 'user':
        #    return None
        return next(root, args, context, info)


schema = graphene.Schema(query=Query)


