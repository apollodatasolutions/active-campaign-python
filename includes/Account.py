
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Account(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=account_add&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def cancel(self, params, post_data = {}):
        request_url = '%s&api_action=account_cancel&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def edit(self, params, post_data):
        request_url = '%s&api_action=account_edit&api_output=%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=account_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def name_check(self, params, post_data = {}):
        request_url = '%s&api_action=account_name_check&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
    
    def plans(self, params, post_data = {}):
        request_url = '%s&api_action=account_plans&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
            
    def status(self, params, post_data = {}):
        request_url = '%s&api_action=account_status&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
                
    def status_set(self, params, post_data = {}):
        request_url = '%s&api_action=account_status_set&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
                    
    def view(self, params, post_data = {}):
        request_url = '%s&api_action=account_view&api_output=%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
        
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## view
    #print ac.api('account/view')