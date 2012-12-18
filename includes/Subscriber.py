
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Subscriber(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=subscriber_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=subscriber_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=subscriber_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=subscriber_edit&api_output=%s&%s' % (self.url, self.output, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=subscriber_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def paginator(self, params, post_data = {}):
        request_url = '%s&api_action=subscriber_paginator&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def sync(self, params, post_data):
        request_url = '%s&api_action=subscriber_sync&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def view(self, params, post_data = {}):
        if params.startswith('email='):
            action = 'subscriber_view_email'
        elif params.startswith('hash='):
            action = 'subscriber_view_hash'
        elif params.startswith('id='):
            action = 'subscriber_view'
        else:
            action = 'subscriber_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (self.url, action, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
##    subscriber = {
##        'email': 'person@example.com',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1,
##    }
##    print ac.api('subscriber/add', subscriber)

    ## delete
##    print ac.api('subscriber/delete?id=10')

    ## delete_list
##    print ac.api('subscriber/delete_list?ids=9,11')

    ## edit
##    subscriber = {
##        'id': 12,
##        'email': 'person@example.com',
##        'first_name': 'Johnny',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1
##    }
##    print ac.api('subscriber/edit', subscriber)

    ## list
##    print ac.api('subscriber/list?ids=1,12')

    ## paginator
##    print ac.api('subscriber/paginator?sort=&offset=0&limit=20&filter=0')

    ## sync
##    subscriber = {
##        'email': 'person@example.com',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'p[1]': 1,
##        'status[1]': 1,
##    }
##    print ac.api('subscriber/sync', subscriber)

    ## view id
##    print ac.api('subscriber/view?id=12')
    
    ## view email
##    print ac.api('subscriber/view?email=person@example.com')
    
    ## view hash
##    print ac.api('subscriber/view?hash=3eeda4735e93f5407fced5ed45ddae82')

