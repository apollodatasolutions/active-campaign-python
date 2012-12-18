from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import json
import urllib2, urllib

class Design(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def edit(self, params, post_data):
        request_url = '%s&api_action=branding_edit&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response
        
    def view(self, params, post_data):
        request_url = '%s&api_action=branding_view&api_output=%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
        
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    
    ## edit
    branding = {
        'id' : 1,
        'branding_url' : 'http://www.example.com/logo.png',
        'copyright' : 'off',
        'demo' : 'on',
        'footer_html' : 'html',
        'footer_html_valueEditor' : '',
        'groupid' :  3,
        'header_html' : 'html',
        'header_html_valueEditor' : '',
        'site_name' : 'Adulmec.ro',
        'logo_source' : 'url'
        
    }
    #print ac.api('branding/edit', branding)
    
    ## view
    print ac.api('branding/view')
