from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi


access_token = "EAAHsrmgrz0YBAA9W2ffy3UsB0UgAzkdPaZANA7VYMNHVKZCD80y4CVSGEB33ZCfn367SNB4ogJdLmwwbZAkcyZCpqyubToEUp3QnsZA7Av9rLfhrVFnQqgO9uL6EJQPbTDZA58oqBFjZB2oqVSsECKQP7KnQzlZAdJ1QU4yJVgePz4ZCfK7gvHw5Ay"
account_id = 'act_414637205659315'
api = FacebookAdsApi.init(access_token=access_token)


adset_account = AdAccount(fbid=account_id, api=api)
adset = adset_account.create_ad_set(params=params)
