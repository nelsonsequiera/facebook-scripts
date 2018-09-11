from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adimage import AdImage
# First, upload the ad image that you will use in your ad creative
# Please refer to Ad Image Create for details.

access_token = "EAAHsrmgrz0YBAA9W2ffy3UsB0UgAzkdPaZANA7VYMNHVKZCD80y4CVSGEB33ZCfn367SNB4ogJdLmwwbZAkcyZCpqyubToEUp3QnsZA7Av9rLfhrVFnQqgO9uL6EJQPbTDZA58oqBFjZB2oqVSsECKQP7KnQzlZAdJ1QU4yJVgePz4ZCfK7gvHw5Ay"
account_id = 'act_414637205659315'
page_id = 238251770344039
# access_token = 'EAAHsrmgrz0YBAAG1qQZCIZBeZApR6jbqZCdwGNoEWUebVquFpNDPKaLa0o7SPPFlhaZBsMaUyWeKPqgjGGEhZAwVwfOJuuu7mZA1OfNVZA0ni4sus7PRQrZAus8sUPluhFE8IOLKq9hIAclz0NAJDlT5VvrZBWGqLeTzaNr3FgI53Gj96YtLrUtwDk1ejsbCDMjrgKcO7MUq78MtBaMB0pZC19kXwWMAXGm1VIZD'
# account_id = 'act_100311700797020'

api = FacebookAdsApi.init(access_token=access_token)
account = AdAccount(account_id)

image = AdImage(parent_id=account_id, api=api)
image[AdImage.Field.filename] = '3373_ho_00_p_2048x1536.jpg'
image["object_story_spec"] = {
    "page_id": page_id
}
image.remote_create()


# Then, use the image hash returned from above
creative = AdCreative(parent_id=account_id)
creative[AdCreative.Field.title] = 'hotel alchemy'
creative[AdCreative.Field.body] = 'Best buy'
creative[AdCreative.Field.object_url] = 'https://gale.agency'
creative[AdCreative.Field.image_hash] = image['hash']

# Finally, create your ad along with ad creative.
# Please note that the ad creative is not created independently, rather its
# data structure is appended to the ad group
ad = Ad(parent_id=account_id)
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = 23843011472840629
ad[Ad.Field.creative] = creative
ad.remote_create(params={
    'status': Ad.Status.paused,
})
{
    "adset_id": 23843019101680629,
    "creative": {
        "body": "Alchemy hotel",
        "title": "My Creative",
        "object_story_spec": {
                "page_id": 2113012528968688,
                "link_data":
                {
                    "call_to_action":
                    {
                        "type": "LEARN_MORE",
                        "value":
                        {
                            "link": "https://alchemy-hotel.gale.agency/e"
                        }
                    },
                    "description": "dasd",
                    "image_hash": "8f7e7cd5c5d483261a9fae13a547ed2f",
                    "link": "https://alchemy-hotel.gale.agency/e",
                    "message": "asdas",
                    "name": "asd"}
        }
    },
    "name": "My Ad",
    "status": "ACTIVE"
}

{
    'name': 'asd',
    'object_story_spec':
    {
        "link_data":
        {
            "call_to_action":
            {
                "type": "LEARN_MORE",
                "value":
                {
                    "link": "https://alchemy-hotel.gale.agency/e"
                }
            },
            "description": "dasd",
            "image_hash": "47c9b42c8eced9421d0f0fd4bdc4bd68",
            "link": "https://alchemy-hotel.gale.agency/e",
            "message": "asdas",
            "name": "asd"
        },
        "page_id": "586200415058722"
    },
    'url_tags': 'source=facebook&adid=d83e3c72-3dbf-4840-bc00-b844989a5bb5'
}
