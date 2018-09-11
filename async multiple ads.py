import datetime
import json
import requests
import time

from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adasyncrequest import AdAsyncRequest
from facebook_business.adobjects.adasyncrequestset import AdAsyncRequestSet
from facebook_business.api import FacebookAdsApi

# access_token = "EAAHsrmgrz0YBAJpeJmtEWcwXbh6XrRw9OffbG677eAanGiEiueL2mbLsOJSGMZB1G65Yw53oGctc2yqZC08GZBZBIAw8cRfkhZB96cnycoEBfnjS4lslC2yL4mdPnZBGcURxd5VUnKNiAOHXdxyEsS840nBhjVuc3LakIB7NzdeyHW3NHKxzT2"
# account_id = 'act_414637205659315'

access_token = 'EAAHsrmgrz0YBAAG1qQZCIZBeZApR6jbqZCdwGNoEWUebVquFpNDPKaLa0o7SPPFlhaZBsMaUyWeKPqgjGGEhZAwVwfOJuuu7mZA1OfNVZA0ni4sus7PRQrZAus8sUPluhFE8IOLKq9hIAclz0NAJDlT5VvrZBWGqLeTzaNr3FgI53Gj96YtLrUtwDk1ejsbCDMjrgKcO7MUq78MtBaMB0pZC19kXwWMAXGm1VIZD'
account_id = 'act_100311700797020'


api = FacebookAdsApi.init(access_token=access_token)
account = AdAccount(account_id)


def get_ad_obj(adset_id):
    ad_name = 'hotel 50'

    return {
        "adset_id": adset_id,
        "creative":
            {
                "body": "Alchemy hotel",
                "title": "Hotel room",
                "object_story_spec":
                {
                    "page_id": 238251770344039,
                    "link_data":
                    {
                        "call_to_action":
                        {
                            "type": "LEARN_MORE",
                            "value":
                            {
                                "link": "https://alchemy-hotel.gale.agency"
                            }
                        },
                        "description": "luxury",
                        "image_hash": "8f7e7cd5c5d483261a9fae13a547ed2f",
                        "link": "https://alchemy-hotel.gale.agency",
                        "message": "book",
                        "name": "hotel"
                    }
                }
            },
        "name": ad_name,
        "status": "ACTIVE"
    }


def get_adset_obj():
    campaign_id = 23843018788930629

    return {
        'billing_event': 'IMPRESSIONS',
        'campaign_id': campaign_id,
        'end_time': '2018-09-20',
        'is_average_price_pacing': False,
        'lifetime_budget': 5520000,
        'name': 'nelson reach adset ',
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


def run():

    ad_url = "https://graph.facebook.com/v3.0/{}/asyncadrequestsets".format(account_id)
    adset_url = "https://graph.facebook.com/v3.0/{}/async_batch_requests".format(account_id)
    headers = {
        'Content-Type': "application/json"
    }

    querystring = {
        "access_token": access_token
    }

    ads = 1

    # data = []
    # for i in range(0, ads):
    #     data.append(get_adset_obj())

    data = []
    for i in range(1, (ads + 1)):
        # adset_id = 23843029496460629
        adset_id = 120330000016590811

        if i >= 50:
            adset_id = 23843021086130629

        data.append(get_ad_obj(adset_id))

    # print(data)
    # print(type(data))
    payload = {
        "ad_specs": data,
        "name": "nelson async 1",
        "notification_mode": "OFF"
    }
    payload_json = json.dumps(payload)
    start = datetime.datetime.now()
    print('request started at : {}'.format(start))
    response = requests.request("POST", ad_url, data=payload_json, headers=headers, params=querystring)
    print('response.json():{}'.format(response.json()))

    if response.status_code != 200:
        print('response is not 200')
        return

    request_id = response.json()['id']
    request_set = AdAsyncRequestSet(request_id)
    print(request_id)
    res = request_set.remote_read(fields=["id", "owner_id", "name", "total_count",
                                          "success_count", "error_count", "is_completed"])

    end = None
    request_result = None

    time.sleep(10)

    while True:
        res = request_set.remote_read(fields=["id", "owner_id", "name", "total_count",
                                              "success_count", "error_count", "is_completed"])
        print(res)
        if res['is_completed']:
            request_result = request_set.get_requests(fields=["id", "status", "result", "input", "scope_object_id"])
            print('request_result: {}'.format(request_result))
            end = datetime.datetime.now()
            break
        else:
            time.sleep(5)

    print("DONE")
    print('time taken : {}'.format(end - start))
    # res = request_set.remote_read(fields=["id", "owner_id", "name", "total_count",
    #                                       "success_count", "error_count", "is_completed"])
    print('res:{}'.format(res))
    return res, request_result


res = None
while True:
    print('\n\n\n')
    res = run()
    time.sleep(3)
    if res:
        break
print(res[1])

'''

res = <AdAsyncRequestSet> {
    "error_count": 0,
    "id": "23843055299600629",
    "is_completed": true,
    "name": "nelson async 1",
    "owner_id": "414637205659315",
    "success_count": 1,
    "total_count": 1
}

request_result = [<AdAsyncRequest> {
    "id": "23843055299610629",
    "input": {
        "account_id": 414637205659315,
        "adgroup_spec": {
            "adset_id": "23843029496460629",
            "creative": {
                "body": "Alchemy hotel",
                "object_story_spec": {
                    "link_data": {
                        "call_to_action": {
                            "type": "LEARN_MORE",
                            "value": {
                                "link": "https://alchemy-hotel.gale.agency/"
                            }
                        },
                        "collection_thumbnails": {},
                        "description": "luxury",
                        "image_crops": {},
                        "image_hash": "8f7e7cd5c5d483261a9fae13a547ed2f",
                        "link": "https://alchemy-hotel.gale.agency/",
                        "message": "book",
                        "multi_share_end_card": true,
                        "multi_share_optimized": true,
                        "name": "hotel",
                        "preferred_image_tags": {},
                        "retailer_item_ids": {}
                    },
                    "page_id": 238251770344039
                },
                "title": "Hotel room"
            },
            "name": "hotel 50",
            "status": "ACTIVE"
        },
        "platform_version": "v3.0"
    },
    "result": {
        "id": "23843055299730629"
    },
    "scope_object_id": "23843029496460629",
    "status": "SUCCESS"
}]

'''
