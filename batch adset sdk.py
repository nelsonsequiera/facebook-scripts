import datetime
import time

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi


def run():

    access_token = "EAAHsrmgrz0YBAJg8YqkhGJGygd6EtTuqMyNYHtU1167JaOBGhGVUi4zmEbIHaAGCMpZC9WDDC9eOCqjHPAynQ0cyAwPT0Wndu6T5MQJJzxup5mPnLZBqqlQVFoNtA8q5YDkdnZCFJ2cVyMFNlOzZBoPfJENilDcWmgAzTPnwGkDvP9Qp7fb2"
    account_id = 'act_414637205659315'

    def get_params(i):
        campaign_id = 23843018788930629

        params = {
            'billing_event': 'IMPRESSIONS',
            'campaign_id': campaign_id,
            'end_time': '2018-09-20',
            'lifetime_budget': 5520000,
            'bid_amount': 2000,
            'name': 'abc reach adset batch async - {}'.format(i),
            'optimization_goal': 'REACH',
            'pacing_type': ['standard'],
            'start_time': '2018-08-13',
            'status': 'PAUSED',
            'targeting':
                {
                    'genders': [1, 2],
                    'facebook_positions': ['feed'],
                    'publisher_platforms': ['facebook'],
                    'geo_locations':
                    {
                        'country_groups': ['worldwide']
                    }
            },
            'flexible_spec': [
                    {
                        'interests': [
                            {
                                'id': '6003442346642'
                            }]
                    }]
        }
        return params

    api = FacebookAdsApi.init(access_token=access_token)
    account = AdAccount(account_id)

    results = list()
    errors = list()

    global global_counter
    global_counter = 0

    def callback_success(response):
        # print('SUCCESS!!!!!!')
        global global_counter
        global_counter += 1
        results.append({global_counter: response})

    def callback_failure(response):
        # print('FAIL!!!!!!')
        global global_counter
        global_counter += 1
        errors.append({global_counter: response})

    adset = AdSet(parent_id=account_id, api=api)
    api_batch = api.new_batch()

    ADSETS_TO_CREATE = 35
    for i in range(1, (ADSETS_TO_CREATE + 1)):
        adset.remote_create(params=get_params(i), batch=api_batch, success=callback_success, failure=callback_failure)

    start = datetime.datetime.now()
    api_batch.execute()
    end = datetime.datetime.now()
    # adaccount = AdAccount(account_id, api=api)
    # params = {
    #     "adbatch": [api_batch],
    #     "name": "nelson async batch"
    # }
    # result = adaccount.create_async_batch_request(params=params)
    # print(result)

    print('--------------')
    print('success: {}'.format(len(results)))
    print('fails: {}'.format(len(errors)))
    print('time taken: {}'.format(end - start))
    print('--------------')

    # for each in results:
    #     for key, value in each.items():
    #         print(key, value.json())

    # --------------
    # success: 35
    # fails: 15
    # --------------


for i in range(0, 10):
    print('start_time: {}'.format(datetime.datetime.now()))
    run()
    print('end_time: {}'.format(datetime.datetime.now()))
    sleep_time = 60 * 9
    print('sleeping for: {}'.format(sleep_time))
    time.sleep(sleep_time)
    print('\n')
