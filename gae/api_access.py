import logging
import http_access

CORE_BASE_URL = 'https://mtv-cherry.musicqubed.com/transport/service/mtv1/7.2/'
#X_USER_AGENT = 'mtv-trax/3.10 (Android; mtv1)'


def get_me_profile(auth_token, x_user_agent):

	PATH = 'me/profile'
	url = CORE_BASE_URL + PATH
	return http_access.fetch_get(url, auth_token = auth_token, x_user_agent = x_user_agent)
	
