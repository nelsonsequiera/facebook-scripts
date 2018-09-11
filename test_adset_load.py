import json
import uuid


def get_name(i):
    return 'facebook 2 nelson - Social - Adset {}'.format(i + 1)


def get_uuid():
    return str(uuid.uuid4())


def data(x):
    data = {
        'account': 'Demo client account - 1',
        'action': 'create',
        'all_required_fields_completed': True,
        'auto_propagate_audience_updates': False,
        'budget': 20000,
        'campaign': [
            {
                'action': 'create',
                'adset': get_adset_data(x),
                'all_required_fields_completed': True,
                'budget': 10000,
                'channels': [
                    'social'
                ],
                'external_id': 'CAM0369',
                'id': get_uuid(),
                'is_complete': True,
                'is_favorite': False,
                'last_state': 'APPROVED',
                'mediaplan_id': 'aa663ec9-5584-4570-9e3c-26b846e73c0a',
                'name': 'nelson local 3 facebook reach campaign',
                'platforms': {
                    'common': {
                        'action': 'no_change',
                        'budget': 0,
                        'external_id': 'PLA0998',
                        'frequency_cap': {
                            'impressions': '23',
                            'period': 'DAY'
                        },
                        'id': '77ee5a13-7744-47e4-b070-9c8e3edd6bbf',
                        'name': 'common',
                        'parent_id': 'd34615cd-370b-4387-ab39-377b80506a88',
                        'status': 'start'
                    },
                    'facebook': {
                        'action': 'create',
                        'bid_cap': 2000,
                        'bid_strategy': 'LOWEST_COST_WITH_BID_CAP',
                        'budget': 10000,
                        'delivery_type': 'standard',
                        'extensions': [

                        ],
                        'external_id': 'PLA0999',
                        'fb_pixel': '217049922179026',
                        'frequency_cap': {
                            'impressions': '23',
                            'period': 'DAY'
                        },
                        'id': '4b13eec1-3fb2-4395-b63b-c9dc4d8402a2',
                        'last_state': 'APPROVED',
                        'location': [
                            {
                                'canonical_name': 'Mysore, India',
                                'country_code': 'IN',
                                'country_name': 'India',
                                'include': True,
                                'key': '1036165',
                                'name': 'Mysore',
                                'search_query': 'myso',
                                'type': 'city',
                                'updated_time': '2018-06-20T09:28:41.203611'
                            }
                        ],
                        'name': 'facebook',
                        'objective': 'reach',
                        'parent_id': 'd34615cd-370b-4387-ab39-377b80506a88',
                        'status': 'start'
                    }
                },
                'report': None,
                'schedule': {
                    'end': '2018-09-01',
                    'start': '2018-08-19'
                },
                'status': 'start',
                'system_error': False
            }
        ],
        'client': {
            'name': 'Democlientaccount-1',
            'site': [
                'https://alchemy-hotel.gale.agency/'
            ]
        },
        'configuration_profile_id': '2516ba4c-3bbd-4ae4-9f98-2b4be5e525f4',
        'configuration_profile_updation_time': '2018-07-11T06:32:46',
        'external_id': 'MED0214',
        'id': 'aa663ec9-5584-4570-9e3c-26b846e73c0a',
        'initiative': None,
        'initiative_id': None,
        'is_complete': True,
        'is_favorite': False,
        'last_state': 'APPROVED',
        'name': 'nelson facebook reach objective',
        'objective': 'awareness',
        'report': None,
        'request_id': 123,
        'schedule': {
            'end': '2018-08-03',
            'start': '2018-07-19'
        },
        'status': 'start',
        'system_error': False
    }
    return data


def get_adset_data(x):
    adsets = list()
    for i in range(0, x):
        adsets.append(adset_data(i))
    return adsets


def adset_data(i):
    data = {'action': 'create',
            'ad': [{'action': 'create',
                    'adset_id': '059d2634-efc0-4960-8f44-1583c8b5166l',
                    'all_required_fields_completed': False,
                    'audit': None,
                    'external_id': 'AD-0155',
                    'id': get_uuid(),
                    'is_favorite': False,
                    'last_state': 'APPROVED',
                    'name': 'nelson facebook reach ad',
                    'platforms': {'facebook': {'action': 'create',
                                               'status': 'start',
                                               'template': [{'ad_format': 'RESPONSIVE',
                                                             'ad_id': get_uuid(),
                                                             'asset_ids': ['nelson_facebook_reach_adset300x250'],
                                                             'asset_url': 'https://cdn.homedit.com/wp-content/uploads/2013/05/Grace-Santorini-Hotel-300x250.jpg',
                                                             'call_to_action': 'APPLY_NOW',
                                                             'description': 'this is a descriptio',
                                                             'headline': 'this is a healdine',
                                                             'id': '3223498e-04c9-4cf6-b5a8-7a4bf431ba0a',
                                                             'last_state': 'APPROVED',
                                                             'name': 'nelson facebook reach ad-template',
                                                             'sub_headline': 'this is a subheadline',
                                                             'url': 'https://alchemy-hotel.gale.agency/'}]}},
                    'report': None,
                    'status': 'start',
                    'system_error': False}],
            'all_required_fields_completed': True,
            'audience': {'attributes': {'age_groups': [],
                                        'gender': [],
                                        'geography': [],
                                        'income': [],
                                        'interests': []},
                         'audience_id': '32c077cf-2cff-488f-a179-aa485e38bd1b',
                         'id': 'd876e4cc-3ec6-4c7a-a0e1-52ab1772556a',
                         'open': True,
                         'target_list_name': 'Gale - FM',
                         'targeted': False},
            'budget': 10000,
            'campaign_id': 'd34615cd-370b-4387-ab39-377b80506a88',
            'caption': 'test offer',
            'external_id': 'ADS0171',
            'id': get_uuid(),
            'is_complete': True,
            'is_favorite': False,
            'last_state': 'APPROVED',
            'mediaplan_objective': 'Awareness',
            'name': get_name(i),
            'offer': 'Get 10% off on Spa',
            'platforms': {'facebook': {'action': 'create',
                                       'ad_format': 'RESPONSIVE',
                                       'ad_rotation': 'Standard',
                                       'ad_size': ['300x250'],
                                       'billing_event': 'IMPRESSIONS',
                                       'budget': 10000,
                                       'external_id': 'PLA1000',
                                       'frequency_control_specs_event': 'IMPRESSIONS',
                                       'frequency_period': 3,
                                       'id': '40a7fe12-5f6e-46a2-a2ce-b7a1b3290522',
                                       'interests': [{'key': '6003020834693',
                                                      'value': 'Interests >> Entertainment >> Music'}],
                                       'is_average_price_pacing': False,
                                       'name': 'facebook',
                                       'parent_id': '059d2634-efc0-4960-8f44-1583c8b5166l',
                                       'pixel_event': 'CONTENT_VIEW',
                                       'placement': ['fb_feed'],
                                       'status': 'start'}},
            'report': None,
            'schedule': {'end': '2018-09-01', 'start': '2018-08-20'},
            'status': 'start',
            'system_error': False}

    return data


def get_data(x=50):
    data_all = data(x)
    asd = json.dumps(data_all)
    print(asd)

get_data()
