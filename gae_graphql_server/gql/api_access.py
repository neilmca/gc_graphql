import logging
import http_access
import webob.multidict
import json

CORE_BASE_URL = 'https://mtv-cherry.musicqubed.com/transport/service/mtv1/7.2/'
PLS_BASE_URL = 'https://mq-media-cms-qa.appspot.com/api/mtv1/'


def get_me_profile(auth_token, x_user_agent):

	PATH = 'me/profile'
	url = CORE_BASE_URL + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)

def get_me_subscriptions(auth_token, x_user_agent):

	PATH = 'me/subscriptions'
	url = CORE_BASE_URL + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)

def get_me_follows(auth_token, x_user_agent):

	PATH = 'me/follows'
	url = CORE_BASE_URL + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)


def get_playlist_feeds(auth_token, x_user_agent, feedIds):

	PATH = 'playlistFeeds'
	url = PLS_BASE_URL + PATH

	query_params_dict = webob.multidict.MultiDict()
	for id in feedIds:
		query_params_dict.add('id', id)

	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent, query_params_dict = query_params_dict)


def post_installations(x_user_agent, secureToken, timestamp, installationId, deviceId):
	PATH = 'installations'
	url = CORE_BASE_URL + PATH

	query_params_dict = {'secureToken' : secureToken, 'timestamp' : timestamp}
	payload = {'installationID' : installationId, 'deviceID' : deviceId}
	payload_str = json.dumps(payload)	

	return http_access.fetch_post(url, x_user_agent = x_user_agent, payload = payload_str, query_params_dict = query_params_dict)

def put_installations(x_user_agent, secureToken, timestamp, installationId, social_type, social_access_token, social_email, social_id):
	PATH = 'installations/'
	url = CORE_BASE_URL + PATH + installationId + '/' + social_type

	query_params_dict = {'secureToken' : secureToken, 'timestamp' : timestamp}
	userIdentity_obj = {'accessToken' : social_access_token, 'email' : social_email, 'id' : social_id}
	payload = {'userIdentity' : userIdentity_obj}
	payload_str = json.dumps(payload)	

	return http_access.fetch_put(url, x_user_agent = x_user_agent, payload = payload_str, query_params_dict = query_params_dict)
	
