
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class List(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=list_add&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=list_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=list_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=list_edit&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def field_add(self, params, post_data):
        request_url = '%s&api_action=list_field_add&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def field_delete(self, params, post_data = {}):
        request_url = '%s&api_action=list_field_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def field_edit(self, params, post_data):
        request_url = '%s&api_action=list_field_edit&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def field_view(self, params, post_data = {}):
        request_url = '%s&api_action=list_field_view&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=list_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def paginator(self, params, post_data = {}):
        request_url = '%s&api_action=list_paginator&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def view(self, params, post_data = {}):
        request_url = '%s&api_action=list_view&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
    
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
    #list1 = {
    #    'name': 'The List',
    #    'sender_name': 'John Smith',
    #    'sender_addr1': 'Bd. MK',
    #    'sender_city': 'Bucharest',
    #    'sender_zip': '123456',
    #    'sender_country': 'Romania'
    #}    
    #print ac.api('list/add', list1)

    ## delete
    #print ac.api('list/delete?id=2')

    ## delete list
    #print ac.api('list/delete?id=1,2')

    ## edit
    #list1 = {
    #    'id': 11,
    #    'name': 'The List Edited',
    #    'sender_name': 'John Smith',
    #    'sender_addr1': 'Bd. MK',
    #    'sender_city': 'Bucharest',
    #    'sender_zip': '123456',
    #    'sender_country': 'Romania'
    #}    
    #print ac.api('list/edit', list1)

    ## field_add
    #field = {
    #    'title': 'My Field',
    #    'type': 1,
    #    'req': 1,
    #    'show_in_list': 1,
    #    'perstag': '%PERS_11%',
    #    'p[11]': 11,
    #    'options[label]': 'value'
    #}
    #print ac.api('list/field_add', field)

    ## field delete
    #print ac.api('list/field_delete?id=7')

    ## field_edit
    #field = {
    #    'id': 7,
    #    'title': 'My Field Edited',
    #    'type': 1,
    #    'req': 0,
    #    'show_in_list': 1,
    #    'perstag': '%PERS_11%',
    #    'p[11]': 11,
    #    'options[label]': 'value'
    #}
    #print ac.api('list/field_edit', field)

    ## field view
    #print ac.api('list/field_view?ids=7')

    ## list
    #print ac.api('list/list?ids=11,1,10')

    ## paginator
    #print ac.api('list/paginator?sort=&offset=0&limit=20&filter=0&public=0')

    ## view
    #print ac.api('list/view?id=1')
