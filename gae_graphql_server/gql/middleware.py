import logging
import graphene

class AuthorizationMiddleware(object):
    def resolve(self, next, root, args, context, info):
    	#logging.info('AuthorizationMiddleware field_name = %s' % info.field_name)
    	#logging.info('root=%s' % str(root))
    	#logging.info('args=%s' % str(args))
    	#logging.info('context=%s' % str(context))
    	

    	#if context == None or 'auth_token' not in context:
    	#	logging.info('No Auth Token present')
    	#	return None





        #if info.field_name == 'user':
        #    return None
        return next(root, args, context, info)