from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = "EAAHsrmgrz0YBAA9W2ffy3UsB0UgAzkdPaZANA7VYMNHVKZCD80y4CVSGEB33ZCfn367SNB4ogJdLmwwbZAkcyZCpqyubToEUp3QnsZA7Av9rLfhrVFnQqgO9uL6EJQPbTDZA58oqBFjZB2oqVSsECKQP7KnQzlZAdJ1QU4yJVgePz4ZCfK7gvHw5Ay"
account_id = 'act_414637205659315'


def get_params(i):
    campaign_id = 23843018788930629

    params = {
        'billing_event': 'IMPRESSIONS',
        'campaign_id': campaign_id,
        'end_time': '2018-09-20',
        'is_average_price_pacing': False,
        'lifetime_budget': 5520000,
        'name': 'nelson reach adset batch async - {}'.format(i),
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
        'is_autobid': True,
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


def callback_success(response):
    print('SUCCESS!!!!!!')
    results.append(response)


def callback_failure(response):
    print('FAIL!!!!!!')
    errors.append(response)


adset = AdSet(parent_id=account_id, api=api)
api_batch = api.new_batch()

ADSETS_TO_CREATE = 5
for i in range(0, ADSETS_TO_CREATE):
    adset.remote_create(params=get_params(i), batch=api_batch, success=callback_success, failure=callback_failure)
# api_batch.execute()

adaccount = AdAccount(account_id, api=api)
params = {
    "adbatch": [api_batch],
    "name": "nelson async batch"
}
result = adaccount.create_async_batch_request(params=params)


print('--------------')
print('success: {}'.format(len(results)))
print('fails: {}'.format(len(errors)))
print('--------------')
print(result)


# --------------
# success: 35
# fails: 15
# --------------
