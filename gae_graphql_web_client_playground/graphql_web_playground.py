#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""A simple guest book app that demonstrates the App Engine search API."""

import logging
from cgi import parse_qs
from datetime import datetime
import re
import random
import os
import string
import urllib
from urlparse import urlparse

import webapp2
from webapp2_extras import jinja2
import http_post
import base64
import json




_INDEX_NAME = 'track'

# _ENCODE_TRANS_TABLE = string.maketrans('-: .@', '_____')

class BaseHandler(webapp2.RequestHandler):
    """The other handlers inherit from this class.  Provides some helper methods
    for rendering a template."""

    @webapp2.cached_property
    def jinja2(self):
      return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, template_args):
      self.response.write(self.jinja2.render_template(filename, **template_args))



X_USER_AGENT = 'x_user_agent'
AUTH_TOKEN = 'auth_token'
QUERY = 'query'
GQL_SERVER_URL = 'gql_server_url'

AUTH_TOKEN_DEFAULT_VALUE = ''
QUERY_DEFAULT_VALUE = ''
X_USER_AGENT_DEFAULT_VALUE = 'mtv-trax/3.10 (Android; mtv1)'
GQL_SERVER_URL_DEFAULT_VALUE = 'http://localhost:8081'


def json_dump(js_string):
    return json.dumps(js_string, indent=2, separators=(',', ': '))

class MainPage(BaseHandler):
    """Handles search requests for comments."""

    def get(self):
        """Handles a get request with a query."""

        x_user_agent = None
        if X_USER_AGENT in self.request.GET:
            x_user_agent = self.request.GET[X_USER_AGENT]
        else:
            x_user_agent = X_USER_AGENT_DEFAULT_VALUE

        auth_token = None
        if AUTH_TOKEN in self.request.GET:
            auth_token = self.request.GET[AUTH_TOKEN]
        else:
            auth_token = AUTH_TOKEN_DEFAULT_VALUE

        query = None
        if QUERY in self.request.GET:
            query = base64.b64decode(self.request.GET[QUERY])
        else:
            query = QUERY_DEFAULT_VALUE

        gql_server_url = None
        if GQL_SERVER_URL in self.request.GET:
            gql_server_url = self.request.GET[GQL_SERVER_URL]
            #strip trailing /
            gql_server_url = gql_server_url.rstrip('/')
        else:
            gql_server_url = GQL_SERVER_URL_DEFAULT_VALUE

        #logging.info('auth_token = %s' % auth_token)
        #logging.info('x_user_agent = %s' % x_user_agent)
        #logging.info('query = %s' % query)
        #logging.info('gql_server_url = %s' % gql_server_url)

        #make request to GraphQl Server

        content = '{}'
        status = ''
        if x_user_agent != '' and query != '' and gql_server_url != '':
            status, content = http_post.fetch_post(url = gql_server_url, auth_token = auth_token, x_user_agent = x_user_agent, query = query)
            
        content_formatted = ''
        try:
            content_formatted = json.dumps(json.loads(content), indent=2)
        except:
            content_formatted = content
        
        template_values = {
            X_USER_AGENT : x_user_agent,
            AUTH_TOKEN : auth_token,
            QUERY : query,
            GQL_SERVER_URL : gql_server_url,
            'query_results': content_formatted,
            'http_status' : status
        }
        self.render_template('index.html', template_values)





class Query(BaseHandler):
    """Handles requests to index comments."""

    def post(self):
        """Handles a post request."""
 

          

        auth_token = self.request.get(AUTH_TOKEN)
        x_user_agent = self.request.get(X_USER_AGENT)
        query = self.request.get(QUERY)
        gql_server_url = self.request.get(GQL_SERVER_URL)



        #logging.info('auth_token = %s' % auth_token)
        #logging.info('x_user_agent = %s' % x_user_agent)
        #logging.info('query = %s' % query)
        #logging.info('gql_server_url = %s' % gql_server_url)

        queryb64 = base64.b64encode(query)
        
        
        if query and x_user_agent:
            self.redirect('/?' + urllib.urlencode(
                {X_USER_AGENT: x_user_agent.encode('utf-8'), AUTH_TOKEN : auth_token, QUERY : queryb64,  GQL_SERVER_URL : gql_server_url}))
        else:
            self.redirect('/')

logging.getLogger().setLevel(logging.DEBUG)


application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/query', Query)],
    debug=True)



