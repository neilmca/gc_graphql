import logging
import graphene

class MeProfileInstallationSchema(graphene.ObjectType):

    def __init__(self, schemaDict):
        if schemaDict:
            self.schemaDict = schemaDict
        else:
            self.schemaDict = {}
        #logging.info('MeProfileInstallationSchema.__init__ schemaDict = %s' % self.schemaDict )
       

    uuid = graphene.String() 
    def resolve_uuid(self, args, context, info):
        #logging.info('resolve_uuid = %s', self.schemaDict['uuid'])
        return self.schemaDict.get('uuid')

    identityId = graphene.String() 
    def resolve_identityId(self, args, context, info):
        #logging.info('resolve_identityId')
        return self.schemaDict.get('identityId')