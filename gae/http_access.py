import logging
from google.appengine.api import urlfetch


def fetch_post():
	try:
	    form_data = urllib.urlencode(UrlPostHandler.form_fields)
	    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	    result = urlfetch.fetch(
	        url='http://localhost:8080/submit_form',
	        payload=form_data,
	        method=urlfetch.POST,
	        headers=headers)
	    self.response.write(result.content)
	except urlfetch.Error:
	    logging.exception('Caught exception fetching url')

def fetch_get(url, x_user_agent = 'not specified', auth_token = 'not specified'):
	try:
		headers = {'X-User-Agent': x_user_agent, 'Authorization' : auth_token}
		logging.info('fetch_get = %s' % url)
		result = urlfetch.fetch(url = url, headers = headers, method=urlfetch.GET)		
	except urlfetch.Error:
		logging.exception('Caught exception fetching url')


	logging.info('GET status = %s', result.status_code)
	logging.info('GET content = %s', result.content)
	return result.status_code,  result.content	    