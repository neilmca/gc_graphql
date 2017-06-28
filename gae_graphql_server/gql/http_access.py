import logging
from google.appengine.api import urlfetch
import urllib


def fetch_put(url, x_user_agent = 'not specified', payload = '', query_params_dict = None):
	return fetch_it(url, x_user_agent = x_user_agent, payload = payload, query_params_dict = query_params_dict, sendAsPut = True);

def fetch_post(url, x_user_agent = 'not specified', payload = '', query_params_dict = None):
	return fetch_it(url, x_user_agent = x_user_agent, payload = payload, query_params_dict = query_params_dict, sendAsPut = False);

def fetch_it(url, x_user_agent = 'not specified', payload = '', query_params_dict = None, sendAsPut = False):
	try:
	    #body = urllib.urlencode(UrlPostHandler.form_fields)
	    headers = {'Content-Type': 'application/json', 'X-User-Agent': x_user_agent}

	    method = urlfetch.POST
	    if sendAsPut:
	    	method = urlfetch.PUT

	    if query_params_dict:
			encoded_params = urllib.urlencode(query_params_dict)		
			url = url + '?' + encoded_params

	    logging.info('fetch_it = %s' % url)
	    logging.info('fetch_post payload = %s' % payload)
	    result = urlfetch.fetch(url=url, payload=payload, method=method, headers=headers)
	    
	except urlfetch.Error:
	    logging.exception('Caught exception fetching url')

	logging.info('POST status = %s', result.status_code)
	logging.info('POST content = %s', result.content)
	return result.status_code,  result.content	 


def fetch_get(url, x_user_agent = 'not specified', auth_token = 'not specified', query_params_dict = None):
	try:
		headers = {'X-User-Agent': x_user_agent, 'Authorization' : auth_token, 'Accept': 'application/json'}

		if query_params_dict:
			encoded_params = urllib.urlencode(query_params_dict)		
			url = url + '?' + encoded_params

		logging.info('fetch_get = %s' % url)
		result = urlfetch.fetch(url = url, headers = headers, method=urlfetch.GET)		
	except urlfetch.Error:
		logging.exception('Caught exception fetching url')


	logging.info('GET status = %s', result.status_code)
	logging.info('GET content = %s', result.content)
	return result.status_code,  result.content	    