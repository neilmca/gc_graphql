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
QUERY = 'query'
GQL_SERVER_URL = 'gql_server_url'
CORE_SERVER_URL = 'core_server_url'
PLS_SERVER_URL = 'pls_server_url'

QUERY_DEFAULT_VALUE = ''
X_USER_AGENT_DEFAULT_VALUE = 'mtv-trax/3.10 (Android; mtv1)'
GQL_SERVER_URL_DEFAULT_VALUE = 'http://localhost:8081'
CORE_SERVER_URL_DEFAULT_VALUE = 'https://mtv-cherry.musicqubed.com/transport/service/mtv1/7.2'
PLS_SERVER_URL_DEFAULT_VALUE = 'https://mq-media-cms-qa.appspot.com/api/mtv1'


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

        core_server_url = None
        if CORE_SERVER_URL in self.request.GET:
            core_server_url = self.request.GET[CORE_SERVER_URL]
            #strip trailing /
            core_server_url = core_server_url.rstrip('/')
        else:
            core_server_url = CORE_SERVER_URL_DEFAULT_VALUE

        pls_server_url = None
        if PLS_SERVER_URL in self.request.GET:
            pls_server_url = self.request.GET[PLS_SERVER_URL]
            #strip trailing /
            pls_server_url = pls_server_url.rstrip('/')
        else:
            pls_server_url = PLS_SERVER_URL_DEFAULT_VALUE


        #logging.info('x_user_agent = %s' % x_user_agent)
        #logging.info('query = %s' % query)
        #logging.info('gql_server_url = %s' % gql_server_url)

        #make request to GraphQl Server

        content = '{}'
        status = ''
        if x_user_agent != '' and query != '' and gql_server_url != '':
            status, content = http_post.fetch_post(gql_url = gql_server_url, core_server_url = core_server_url, pls_server_url = pls_server_url, x_user_agent = x_user_agent, query = query)
            
        content_formatted = ''
        try:
            content_formatted = json.dumps(json.loads(content), indent=2)
        except:
            content_formatted = content
        
        template_values = {
            X_USER_AGENT : x_user_agent,
            QUERY : query,
            GQL_SERVER_URL : gql_server_url,
            CORE_SERVER_URL : core_server_url,
            PLS_SERVER_URL : pls_server_url,
            'query_results': content_formatted,
            'http_status' : status
        }
        logging.info(template_values)
        self.render_template('index.html', template_values)





class Query(BaseHandler):
    """Handles requests to index comments."""

    def post(self):
        """Handles a post request."""
 

          

        x_user_agent = self.request.get(X_USER_AGENT)
        query = self.request.get(QUERY)
        gql_server_url = self.request.get(GQL_SERVER_URL)



        
        #logging.info('x_user_agent = %s' % x_user_agent)
        #logging.info('query = %s' % query)
        #logging.info('gql_server_url = %s' % gql_server_url)

        queryb64 = base64.b64encode(query)
        
        
        if query and x_user_agent:
            self.redirect('/?' + urllib.urlencode(
                {X_USER_AGENT: x_user_agent.encode('utf-8'), QUERY : queryb64,  GQL_SERVER_URL : gql_server_url}))
        else:
            self.redirect('/')

logging.getLogger().setLevel(logging.DEBUG)


application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/query', Query)],
    debug=True)




