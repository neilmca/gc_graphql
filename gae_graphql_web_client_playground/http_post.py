import logging
from google.appengine.api import urlfetch


def fetch_post(url, auth_token, x_user_agent, query):
	try:
	    #form_data = urllib.urlencode(UrlPostHandler.form_fields)
	    
	    headers = {'X-User-Agent': x_user_agent, 'Authorization' : 'Bearer ' + auth_token}
	    
	    result = urlfetch.fetch(
	        url=url,
	        payload=query,
	        method=urlfetch.POST,
	        headers=headers)
	    return result.status_code,  result.content	
	except urlfetch.Error:
	    logging.exception('Caught exception fetching url')