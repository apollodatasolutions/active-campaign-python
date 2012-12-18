from includes.ActiveCampaign import ActiveCampaign
from includes.Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY

if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## delete subscriber
    #print ac.api('subscriber/delete?id=10')

    ## delete_list
    #print ac.api('subscriber/delete_list?ids=9,11')

    # edit subscriber
    subscriber = {
       'id': 12,
       'email': 'person@example.com',
       'first_name': 'John',
       'last_name': 'Smith',
       'p[1]': 1,
       'status[1]': 1,
    }
    print ac.api('subscriber/edit', subscriber)
