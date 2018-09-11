import time

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

access_token = "EAAHsrmgrz0YBAA9W2ffy3UsB0UgAzkdPaZANA7VYMNHVKZCD80y4CVSGEB33ZCfn367SNB4ogJdLmwwbZAkcyZCpqyubToEUp3QnsZA7Av9rLfhrVFnQqgO9uL6EJQPbTDZA58oqBFjZB2oqVSsECKQP7KnQzlZAdJ1QU4yJVgePz4ZCfK7gvHw5Ay"
account_id = 'act_414637205659315'


api = FacebookAdsApi.init(access_token=access_token)
account = AdAccount(account_id)


def create_ad(name, adset_id, creative_id, status):
    print('Creating Ad: (name={})'.format(name))
    params = {
        Ad.Field.name: name,
        Ad.Field.adset_id: adset_id,
        Ad.Field.creative: {
            'creative_id': creative_id,
        },
        Ad.Field.status: status,
    }

    ad = Ad(parent_id=account_id, api=api)
    # ad = ad.remote_create(params=params)
    # print(ad)
    return ad

ad_list = []
for i in range(0, 10):


params = {
    # 'level': 'campaign',
    'campaign_id': 23842986818330629
}

i_async_job = account.get_insights(params=params, async=True)

# Insights
while True:
    job = i_async_job.remote_read()
    print(job)
    print("Percent done: " + str(job['async_percent_completion']))
    time.sleep(1)
    if job['async_status'] == "Job Completed":
        print("Done!")
        break

print(i_async_job.get_result())
