import datetime
import json
import time

from django.conf import settings

redis = settings.REDIS_CLIENT
REDIS_REQUEST_SET_NAME = 'facebook_request_log_set'

number_of_requests = 100


def log_request(level, action, i):
    time_of_arrival = datetime.datetime.utcnow()
    score = time_of_arrival.timestamp() * 1000
    data = {
        'level': level,
        'action': action,
        'time_of_arrival_in_utc': str(time_of_arrival)
    }
    datas = json.dumps(data)

    print("adding request number: {}".format(i + 1))

    redis.zadd(REDIS_REQUEST_SET_NAME, datas, score)


def get_requests_last_x_mins(mins=10):
    current_time = datetime.datetime.utcnow()
    x_minutes_ago = current_time - datetime.timedelta(minutes=mins)
    x_minutes_ago_epoch_ts = x_minutes_ago.timestamp() * 1000

    current_time = datetime.datetime.utcnow()
    current_time = current_time.timestamp() * 1000
    result = redis.zrangebyscore(REDIS_REQUEST_SET_NAME, x_minutes_ago_epoch_ts, current_time, withscores=True)
    return result


def get_sleep_time(level, action):
    """
    returns:
        sleep_time (float) = (number of requests in last 10 mins * sleep factor)
    """
    sleep_time_factor = 0.5  # increase this if current sleep time is not stopping rate limit. eg: 1.3

    requests = get_requests_last_x_mins()
    sleep_time = len(requests) * sleep_time_factor
    return sleep_time


for i in range(0, number_of_requests):
    time_to_sleep = get_sleep_time('create', 'audience')
    print('time_to_sleep: {}'.format(time_to_sleep))
    time.sleep(time_to_sleep)
    log_request('create', 'audience', i)  # log the request
    print('\n')
