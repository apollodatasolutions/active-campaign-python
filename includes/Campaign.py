from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from ActiveCampaign import ActiveCampaign
import simplejson as json
import urllib2, urllib
import datetime, time

class Campaign(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def create(self, params, post_data):
        request_url = '%s&api_action=campaign_create&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def paginator(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_paginator&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
    
    def report_bounce_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_bounce_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_bounce_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_bounce_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_forward_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_forward_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_forward_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_forward_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_link_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_link_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_link_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_link_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_open_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_open_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_open_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_open_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unopen_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unopen_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unsubscription_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unsubscription_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unsubscription_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unsubscription_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def send(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_send&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def status(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_status&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
    
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## create
    sdate = datetime.datetime.now() + datetime.timedelta(hours = 0, minutes = 2)
    campaign = {
        'type': 'single',
        'name': 'testActiveCampaign: %s' % datetime.datetime.now(),
        'sdate': time.strftime('%Y-%m-%d %H:%M:%S', sdate.timetuple()),
        'status': 1,
        'public': 1,
        'tracklinks': 'all',
        'trackreads': 1,
        'htmlunsub': 1,
        'p[1]': 1,
        'm[35]': 100
    }
    from time import time
    time2 = time()
    print ac.api('campaign/create', campaign)
    print 'diff2 = %.5f seconds' %(time() - time2)
    

    ## delete
##    print ac.api('campaign/delete?id=12')

    ## delete_list
##    print ac.api('campaign/delete_list?ids=1,2')

    ## list
##    print ac.api('campaign/list?ids=3,4')

    ## paginator
##    print ac.api('campaign/paginator?sort=&offset=0&limit=20&filter=0&public=0')

    ## report_bounce_list
##    print ac.api('campaign/report_bounce_list?campaignid=3')

    ## report_bounce_totals
##    print ac.api('campaign/report_bounce_totals?campaignid=13&messageid=2')

    ## report_forward_list
##    print ac.api('campaign/report_forward_list?campaignid=13&messageid=2')

    ## report_forward_totals
##    print ac.api('campaign/report_forward_totals?campaignid=13&messageid=2')

    ## report_link_list
##    print ac.api('campaign/report_link_list?campaignid=13&messageid=2')

    ## report_link_totals
##    print ac.api('campaign/report_link_totals?campaignid=13&messageid=2')

    ## report_open_list
##    print ac.api('campaign/report_open_list?campaignid=13&messageid=2')

    ## report_open_totals
##    print ac.api('campaign/report_open_totals?campaignid=13&messageid=2')

    ## report_totals
##    print ac.api('campaign/report_totals?campaignid=13&messageid=2')

    ## report_unopen_list
##    print ac.api('campaign/report_unopen_list?campaignid=13&messageid=2')

    ## report_unsubscription_list
##    print ac.api('campaign/report_unsubscription_list?campaignid=13')

    ## report_unsubscription_totals
##    print ac.api('campaign/report_unsubscription_totals?campaignid=13&messageid=2')

    ## report_send
##    print ac.api('campaign/send?campaignid=13&messageid=2&type=mime&action=send&email=person@example.com')

    ## report_status
##    print ac.api('campaign/status?id=13&status=5')
