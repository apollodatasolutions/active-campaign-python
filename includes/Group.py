
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Group(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=group_add&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response
        
    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=group_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=group_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def edit(self, params, post_data):
        request_url = '%s&api_action=group_edit&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response
        
    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=group_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def view(self, params, post_data = {}):
        request_url = '%s&api_action=group_view&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    
    ## add
    # group = {
    #    'title': 'second-test-group',
    #    'descript' : 'This group is created from API',
    #    'lists[1]' : 1,
    #    'pg_form_edit' : 1,
    #    'pg_subscriber_add' : 1,
    #    'pg_subscriber_delete' : 0
    # }    
    # print ac.api('group/add', group)
    
    ## delete_list
    #print ac.api('group/delete_list?ids=4,5')
    
    ## delete
    #print ac.api('group/delete?id=6')
    
    ## edit
    # group = {
    #    'title': 'second-group',
    #    'id' : 7
    # }    
    # print ac.api('group/edit', group)
    
    ## list
    #print ac.api('group/list?ids=1,7')

    ## view
    #print ac.api('group/view?id=7')
