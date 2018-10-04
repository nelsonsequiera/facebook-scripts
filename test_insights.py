import datetime
import json
import requests
import time


access_token_1 = "<INSERT_TOKEN>"
access_token_2 = "<INSERT_TOKEN>"
access_token_3 = "<INSERT_TOKEN>"
access_token_4 = "<INSERT_TOKEN>"
arr = [access_token_1, access_token_2, access_token_3, access_token_4]
access_tokens = {
    access_token_1: 4,
    access_token_2: 2,
    access_token_3: 3,
    access_token_4: 1
}


def get_token():
    print('getting token')
    token_key = None
    for key, val in access_tokens.items():
        if val == 1:
            token_key = key
            break

    for key, val in access_tokens.items():
        if val == 4:
            access_tokens[key] = 1
        else:
            access_tokens[key] += 1
    print("*" * 50)
    print(token_key[-1])
    print("*" * 50)
    return token_key


rotate = 0


def get_token2():
    global rotate
    token_key = arr[rotate]
    rotate = (rotate + 1) % 4
    return token_key


def test_insights(access_token):
    url = "https://graph.facebook.com/v2.12/23842954292550629/insights"

    querystring = {"fields": "account_currency,account_id,account_name,action_values,actions,ad_id,ad_name,adset_id,adset_name,buying_type,call_to_action_clicks,campaign_id,campaign_name,canvas_avg_view_percent,canvas_avg_view_time,clicks,cost_per_10_sec_video_view,cost_per_action_type,cost_per_estimated_ad_recallers,cost_per_inline_link_click,cost_per_inline_post_engagement,cost_per_outbound_click,cost_per_total_action,cost_per_unique_action_type,cost_per_unique_click,cost_per_unique_inline_link_click,cost_per_unique_outbound_click,cpc,cpm,cpp,ctr,date_start,date_stop,estimated_ad_recall_rate,estimated_ad_recallers,frequency,impressions,inline_link_click_ctr,inline_link_clicks,inline_post_engagement,mobile_app_purchase_roas,objective,outbound_clicks,outbound_clicks_ctr,place_page_name,reach,relevance_score,social_clicks,social_impressions,social_reach,social_spend,spend,total_action_value,total_actions,total_unique_actions,unique_actions,unique_clicks,unique_ctr,unique_inline_link_click_ctr,unique_inline_link_clicks,unique_link_clicks_ctr,unique_outbound_clicks,unique_outbound_clicks_ctr,unique_social_clicks,video_10_sec_watched_actions,video_30_sec_watched_actions,video_avg_percent_watched_actions,video_avg_time_watched_actions,video_p100_watched_actions,video_p25_watched_actions,video_p50_watched_actions,video_p75_watched_actions,video_p95_watched_actions,website_ctr,website_purchase_roas", "access_token": access_token}

    payload = "fields=impressions&access_token={}".format(access_token)
    headers = {}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.headers['x-app-usage'])

    return response


def create_ad(access_token, counter):
    url = "https://graph.facebook.com/v2.12/act_414637205659315/ads"
    payload = {
        'access_token': access_token,
        'adset_id': '23843017094920629',
        'creative': {'creative_id': '23843017095200629'},
        'name': 'load test {}'.format(counter),
        'status': 'ACTIVE'
    }
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "a7a1e7dd-64b0-4a6d-8e2d-bf0174c7928b"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    print(response.headers['x-app-usage'])
    return response


def run_task():
    counter = 0
    access_token = None

    time_btwn_each_req = 1
    time_for_user_limit = 60

    access_token = get_token()
    print('Time between each request: {}'.format(time_btwn_each_req))
    resp = None

    log = '-' * 100

    last_counter = 0

    start_time = datetime.datetime.now()
    last_time = start_time
    while True:
        # time.sleep(3)
        counter += 1
        resp = create_ad(access_token, counter)
        time.sleep(time_btwn_each_req)
        print('request number: {}'.format(counter))
        if not resp.ok:
            access_token = get_token()
            end_time = datetime.datetime.now()
            time_taken = 'time taken before limit: {}'.format(end_time - last_time)

            log += '\n time taken before error: {time_taken}'.format(time_taken=time_taken)
            log += '\n number of requests succeeded: {counter}'.format(counter=(counter - last_counter))
            log += '\n error that occured: {}\n'.format(resp.json())
            log += '-' * 100
            print(log)

            last_counter = counter
            last_time = end_time
            if resp.json()['error']['code'] == 613:
                break

            if resp.json()['error']['code'] == 17:
                time.sleep(time_for_user_limit)

    print('FINAL REPORT:')
    print('Time between each request: {}'.format(time_btwn_each_req))
    print('total time taken: {}'.format(last_time - start_time))
    print('Number of reqests succeeded: {}'.format(counter))
    print(log)


time_to_sleep = 8 * 60

while True:
    run_task()
    print(datetime.datetime.now())
    print('sleeping for: {}'.format(time_to_sleep))
    time.sleep(time_to_sleep)
    # time_to_sleep = (time_to_sleep - 30)
