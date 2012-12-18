from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Form(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def getforms(self, params, post_data = {}):
        request_url = '%s&api_action=form_getforms&api_output=%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
    def html(self, params, post_data = {}):
        request_url = '%s&api_action=form_html&api_output=%s&%s' % (self.url, self.output, params)
        #print urllib2.urlopen(request_url).read()
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    
    ## getforms
    #print ac.api('form/getforms')
    
    ## html
    #print ac.api('form/html?id=1142')
