from graphene.test import Client
from ..schema import gql_schema



servicemanifest_query = '''
        query {
          servicemanifest(url: "333") {
             url
          }
        }
    '''

servicemanifest_query_response = {
        'data': {
            'servicemanifest': {
              'url' : '333'
            }
        }
        }

def test_hello():
    print('schema = %s', str(gql_schema.schema))

    client = Client(gql_schema.schema)
    
    executed = client.execute(servicemanifest_query, middleware = [gql_schema.LoggerMiddleware()])
    print('executed = %s' % str(executed))
    assert executed == servicemanifest_query_response
    return