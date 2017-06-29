import logging
import http_access
import webob.multidict
import json

CORE_BASE_URL = 'https://mtv-cherry.musicqubed.com/transport/service/mtv1/7.2/'
PLS_BASE_URL = 'https://mq-media-cms-qa.appspot.com/api/mtv1/'
CORE_BASE_URL_KEY = 'core_server_url'
PLS_BASE_URL_KEY = 'pls_server_url'


def get_me_profile(service_urls, auth_token, x_user_agent):

	PATH = 'me/profile'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)

def get_me_subscriptions(service_urls, auth_token, x_user_agent):

	PATH = 'me/subscriptions'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)

def get_me_follows(service_urls, auth_token, x_user_agent):

	PATH = 'me/follows'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)


def get_playlist_feeds(service_urls, auth_token, x_user_agent, feedIds):

	PATH = 'playlistFeeds'
	url = service_urls.get(PLS_BASE_URL_KEY) + '/' + PATH
	query_params_dict = webob.multidict.MultiDict()
	for id in feedIds:
		query_params_dict.add('id', id)

	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent, query_params_dict = query_params_dict)


def post_installations(service_urls, x_user_agent, secureToken, timestamp, installationId, deviceId):
	PATH = 'installations'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH
	
	query_params_dict = {'secureToken' : secureToken, 'timestamp' : timestamp}
	payload = {'installationID' : installationId, 'deviceID' : deviceId}
	payload_str = json.dumps(payload)	

	return http_access.fetch_post(url, x_user_agent = x_user_agent, payload = payload_str, query_params_dict = query_params_dict)

def put_installations(service_urls, x_user_agent, secureToken, timestamp, installationId, social_type, social_access_token, social_email, social_id):
	PATH = 'installations/'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH  + installationId + '/' + social_type
	
	query_params_dict = {'secureToken' : secureToken, 'timestamp' : timestamp}
	userIdentity_obj = {'accessToken' : social_access_token, 'email' : social_email, 'id' : social_id}
	payload = {'userIdentity' : userIdentity_obj}
	payload_str = json.dumps(payload)	

	return http_access.fetch_put(url, x_user_agent = x_user_agent, payload = payload_str, query_params_dict = query_params_dict)

def get_acc_check(service_urls, user_token, x_user_agent, timestamp, user_name, device_uid):
	PATH = 'ACC_CHECK'
	url = service_urls.get(CORE_BASE_URL_KEY) + '/' + PATH

	query_params_dict = {'USER_TOKEN' : user_token, 'timestamp' : timestamp, 'USER_NAME' : user_name,  'DEVICE_UID' : device_uid}	
	return  http_access.fetch_get(url, x_user_agent = x_user_agent, query_params_dict = query_params_dict)

	
