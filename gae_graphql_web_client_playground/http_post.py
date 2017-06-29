import logging
from google.appengine.api import urlfetch


def fetch_post(gql_url, core_server_url, pls_server_url, x_user_agent, query):
	try:
	    #form_data = urllib.urlencode(UrlPostHandler.form_fields)
	    
	    headers = {'X-User-Agent': x_user_agent, 'core_server_url' : core_server_url, 'pls_server_url' : pls_server_url}
	    
	    result = urlfetch.fetch(
	        url=gql_url,
	        payload=query,
	        method=urlfetch.POST,
	        headers=headers)
	    return result.status_code,  result.content	
	except urlfetch.Error:
	    logging.exception('Caught exception fetching url')