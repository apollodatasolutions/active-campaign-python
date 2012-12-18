import json
from Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
import urllib2

class Connector():

    def __init__(self, url, api_key, api_user = '', api_pass = ''):
        self.output = 'json'
        self.base = ''
        
        if url != 'https://www.activecampaign.com':
            # not set reseller
            self.base = '/admin'
        if url[-1] == '/':
            # remove trailing slash
            url = url[:-1]

        if api_key:
            self.url = '%s%s/api.php?api_key=%s' % (url, self.base, api_key)
        else:
            self.url = '%s%s/api.php?api_user=%s&api_pass=%s' % (url, self.base, api_user, api_pass)
        self.api_key = api_key

    def credentials_test(self):
        test_url = '%s&api_action=group_view&api_output=%s&id=3' % (self.url, self.output)
        jdata = json.loads(urllib2.urlopen(test_url).read())
        return jdata['result_code'] == 1

if __name__ == '__main__':
    c = Connector(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    print c.credentials_test()
